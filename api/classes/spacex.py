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

    def get_all_launches(self) -> list[Launch]:
        endpoint = "/v4/launches"
        launches = self._conn.get(endpoint=endpoint)
        launches_list = [Launch(**launch) for launch in launches]
        return launches_list

    def get_all_launchpads(self) -> list[Launchpad]:
        endpoint = "/v4/launchpads"
        launchpads = self._conn.get(endpoint=endpoint)
        launchpad_list = [Launchpad(**launchpad) for launchpad in launchpads]
        return launchpad_list
