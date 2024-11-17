from logging import Logger
from unittest.mock import create_autospec

import pytest

from api.classes.connection import SpacexConnection
from api.classes.spacex import SpaceX
from api.classes.entities import Launch
from api import create_app


@pytest.fixture
def example_launch_json():
    return {
        "fairings": {
            "reused": False,
            "recovery_attempt": False,
            "recovered": False,
            "ships": ["someid"],
        },
        "links": {
            "patch": {
                "small": "https://images2.imgbox.com/94/f2/NN6Ph45r_o.png",
                "large": "https://images2.imgbox.com/5b/02/QcxHUb5V_o.png",
            },
            "reddit": {
                "campaign": "null",
                "launch": "null",
                "media": "null",
                "recovery": "null",
            },
            "flickr": {"small": ["some"], "original": ["some"]},
            "presskit": "some",
            "webcast": "https://www.youtube.com/watch?v=0a_00nJ_Y88",
            "youtube_id": "0a_00nJ_Y88",
            "article": "https://www.space.com/2196-spacex-inaugural-falcon-1-rocket-lost-launch.html",
            "wikipedia": "https://en.wikipedia.org/wiki/DemoSat",
        },
        "static_fire_date_utc": "2006-03-17T00:00:00.000Z",
        "static_fire_date_unix": 1142553600,
        "net": False,
        "window": 0,
        "rocket": "5e9d0d95eda69955f709d1eb",
        "success": False,
        "failures": [
            {"time": 33, "altitude": 342, "reason": "merlin engine failure"}
        ],
        "details": "Engine failure at 33 seconds and loss of vehicle",
        "crew": [],
        "ships": [],
        "capsules": [],
        "payloads": ["5eb0e4b5b6c3bb0006eeb1e1"],
        "launchpad": "5e9e4502f5090995de566f86",
        "flight_number": 1,
        "name": "FalconSat",
        "date_utc": "2006-03-24T22:30:00.000Z",
        "date_unix": 1143239400,
        "date_local": "2006-03-25T10:30:00+12:00",
        "date_precision": "hour",
        "upcoming": False,
        "cores": [
            {
                "core": "5e9e289df35918033d3b2623",
                "flight": 1,
                "gridfins": False,
                "legs": False,
                "reused": False,
                "landing_attempt": False,
                "landing_success": False,
                "landing_type": "Ocean",
                "landpad": "5e9e3032383ecb761634e7cb",
            }
        ],
        "auto_update": True,
        "tbd": False,
        "launch_library_id": "5eb87cd9ffd86e000604b32a",
        "id": "5eb87cd9ffd86e000604b32a",
    }


@pytest.fixture
def example_launchpad_json():
    return {
        "images": {"large": ["https://i.imgur.com/7uXe1Kv.png"]},
        "name": "VAFB SLC 3W",
        "full_name": "Vandenberg Space Force Base Space Launch Complex 3W",
        "locality": "Vandenberg Space Force Base",
        "region": "California",
        "latitude": 34.6440904,
        "longitude": -120.5931438,
        "launch_attempts": 0,
        "launch_successes": 0,
        "rockets": ["5e9d0d95eda69955f709d1eb"],
        "timezone": "America/Los_Angeles",
        "launches": ["5eb87cddffd86e000604b32f"],
        "status": "retired",
        "details": "SpaceX's original west coast launch pad for Falcon 1. It was used in a static fire test but was never employed for a launch, and was abandoned due to range scheduling conflicts arising from overflying other active pads.",
        "id": "5e9e4501f5090910d4566f83",
    }


@pytest.fixture
def example_launches(example_launch_json):
    return [Launch(**example_launch_json), Launch(**example_launch_json)]


@pytest.fixture
def mock_logger():
    mock_logger = create_autospec(spec=Logger)
    mock_logger_instance = mock_logger.return_value
    return mock_logger_instance


@pytest.fixture
def mock_connection():
    mock_conn = create_autospec(spec=SpacexConnection)
    mock_conn_instance = mock_conn.return_value
    return mock_conn_instance


@pytest.fixture
def mock_spacex():
    mock_spacex = create_autospec(spec=SpaceX)
    mock_spacex_instance = mock_spacex.return_value
    return mock_spacex_instance


@pytest.fixture
def mock_app(mocker, mock_spacex):
    mocker.patch("api.dictConfig")
    mock_spacex_class = mocker.patch("api.SpaceX")
    mock_spacex_class.return_value = mock_spacex
    app = create_app(config_type="Testing")
    return app
