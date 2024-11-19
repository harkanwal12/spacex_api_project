"""Connection module.

This module implements a connection class which handles the HTTP requests to
the SpaceX-API. This includes logging and exception handling.
"""

import logging

import requests
import requests.packages
from json.decoder import JSONDecodeError
from api.classes.exceptions import NoDataFoundException, BadJSONException


class SpacexConnection:
    def __init__(
        self,
        base_url: str = "https://api.spacexdata.com",
        ssl_verify: bool = True,
        logger: logging.Logger = None,
    ):
        """
        SpaceX Connection Constructor

        :param str base_url: The URL of the SpaceX API. Default is https://api.spacexdata.com
        :param bool ssl_verify: Set SSL Cert Verification for HTTP requests. Default is enabled.
        :param logging.logger logging: Python logger instance. Default will create one automatically.
        """
        self._base_url = base_url
        self._ssl_verify = ssl_verify
        self._logger = logger or logging.getLogger(__name__)
        if not ssl_verify:
            # noinspection PyUnresolvedReferences
            requests.packages.urllib3.disable_warnings()

    def _request(
        self, method: str, endpoint: str, data=None
    ) -> dict | list[dict]:

        url = self._base_url + endpoint

        log_line_pre = f"url={url}"
        log_line_post = ", ".join(
            (log_line_pre, "success={}, status_code={}, message={}")
        )

        try:
            self._logger.debug(msg=log_line_pre)
            response = requests.request(
                method, url, verify=self._ssl_verify, json=data
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self._logger.error(msg=(str(e)))
            if e.response.status_code == 404:
                description = "No data found for request"
                raise NoDataFoundException(description) from e
            raise e

        is_success = 299 >= response.status_code >= 200
        log_line = f"success={is_success}, status_code={response.status_code}, message={response.reason}"
        self._logger.debug(msg=log_line)

        try:
            response = response.json()
        except (ValueError, JSONDecodeError) as e:
            self._logger.error(msg=log_line_post.format(False, None, e))
            raise BadJSONException("Bad JSON in response") from e

        # Requests with MongoDB Queries store the data in the "docs" key
        if "docs" in response:
            response = response["docs"]

        if not response:
            raise NoDataFoundException("No data found for request")

        return response

    def get(self, endpoint: str) -> dict | list[dict]:
        return self._request(method="GET", endpoint=endpoint)

    def post(self, endpoint: str, data: dict) -> dict | list[dict]:
        return self._request(method="POST", endpoint=endpoint, data=data)
