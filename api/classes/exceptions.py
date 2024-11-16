"""Exceptions module.

This module contains all custom exceptions.
"""


class NoDataFoundException(Exception):
    """The SpaceX API returns a 404 when no data is found"""

    pass


class BadJSONException(Exception):
    """Raise when JSON extraction from response goes wrong"""

    pass
