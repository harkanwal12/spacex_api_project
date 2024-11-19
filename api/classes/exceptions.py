"""Exceptions module.

This module contains all custom exceptions.
"""


class NoDataFoundException(Exception):
    """Handles the 404 not found error returned by the SpaceX API"""

    pass


class BadJSONException(Exception):
    """Raise when JSON extraction from response goes wrong"""

    pass
