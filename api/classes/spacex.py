"""SpaceX-API Wrapper module.

This module is a user-friendly interface between the SpaceX-API 
and the dataclass abstractions provided by this library.
Construct the SpaceX class below. See README docs for more info.
"""

import logging

from api.classes.connection import SpacexConnection
from api.classes.entities import Launch, Launchpad


class SpaceX:
    def __init__(
        self,
        base_url: str = "https://api.spacexdata.com",
        ssl_verify: bool = True,
        logger: logging.Logger = None,
    ):
        """
        SpaceX Client Constructor

        :param str base_url: The URL of the SpaceX API. Default is https://api.spacexdata.com
        :param bool ssl_verify: Set SSL Cert Verification for HTTP requests. Default is enabled.
        :param logging.logger logging: Python logger instance. Default will create one automatically.
        """
        self._conn = SpacexConnection(base_url, ssl_verify, logger)

    def get_launches(
        self, launch_id: str = None, query: dict = None
    ) -> list[Launch]:
        endpoint = "/v4/launches"
        launches = self._request_handler(endpoint, launch_id, query)
        if isinstance(launches, list):
            return [Launch(**launch) for launch in launches]
        else:
            return [Launch(**launches)]

    def get_launchpads(
        self, launchpad_id: str = None, query: dict = None
    ) -> list[Launchpad]:
        endpoint = "/v4/launchpads"
        launchpads = self._request_handler(endpoint, launchpad_id, query)
        if isinstance(launchpads, list):
            return [Launchpad(**launch) for launch in launchpads]
        else:
            return [Launchpad(**launchpads)]

    def _request_handler(
        self, endpoint: str, id: str = None, query: dict = None
    ) -> list[dict] | dict:
        if id:
            data = self._conn.get(f"{endpoint + '/' + id}")
        elif query:
            data = self._conn.post(f"{endpoint + '/query'}", data=query)
        else:
            data = self._conn.get(endpoint)

        return data
