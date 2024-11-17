from logging import Logger
from unittest.mock import create_autospec

import pytest

from api.classes.connection import SpacexConnection
from api.classes.spacex import SpaceX
from api.classes.entities import Launch, Launchpad
from api import create_app


@pytest.fixture
def example_launch_json():
    return [
        {
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
                {
                    "time": 33,
                    "altitude": 342,
                    "reason": "merlin engine failure",
                }
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
        },
        {
            "fairings": {
                "reused": False,
                "recovery_attempt": False,
                "recovered": False,
                "ships": [],
            },
            "links": {
                "patch": {
                    "small": "https://images2.imgbox.com/f9/4a/ZboXReNb_o.png",
                    "large": "https://images2.imgbox.com/80/a2/bkWotCIS_o.png",
                },
                "reddit": {
                    "campaign": "null",
                    "launch": "null",
                    "media": "null",
                    "recovery": "null",
                },
                "flickr": {"small": [], "original": []},
                "presskit": "null",
                "webcast": "https://www.youtube.com/watch?v=Lk4zQ2wP-Nc",
                "youtube_id": "Lk4zQ2wP-Nc",
                "article": "https://www.space.com/3590-spacex-falcon-1-rocket-fails-reach-orbit.html",
                "wikipedia": "https://en.wikipedia.org/wiki/DemoSat",
            },
            "static_fire_date_utc": "null",
            "static_fire_date_unix": "null",
            "net": False,
            "window": 0,
            "rocket": "5e9d0d95eda69955f709d1eb",
            "success": False,
            "failures": [
                {
                    "time": 301,
                    "altitude": 289,
                    "reason": "harmonic oscillation leading to premature engine shutdown",
                }
            ],
            "details": "Successful first stage burn and transition to second stage, maximum altitude 289 km, Premature engine shutdown at T+7 min 30 s, Failed to reach orbit, Failed to recover first stage",
            "crew": [],
            "ships": [],
            "capsules": [],
            "payloads": ["5eb0e4b6b6c3bb0006eeb1e2"],
            "launchpad": "5e9e4502f5090995de566f86",
            "flight_number": 2,
            "name": "DemoSat",
            "date_utc": "2007-03-21T01:10:00.000Z",
            "date_unix": 1174439400,
            "date_local": "2007-03-21T13:10:00+12:00",
            "date_precision": "hour",
            "upcoming": False,
            "cores": [
                {
                    "core": "5e9e289ef35918416a3b2624",
                    "flight": 1,
                    "gridfins": False,
                    "legs": False,
                    "reused": False,
                    "landing_attempt": False,
                    "landing_success": "null",
                    "landing_type": "null",
                    "landpad": "null",
                }
            ],
            "auto_update": True,
            "tbd": False,
            "launch_library_id": "null",
            "id": "5eb87cdaffd86e000604b32b",
        },
    ]


@pytest.fixture
def example_launchpad_json():
    return [
        {
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
            "launches": ["5eb87cd9ffd86e000604b32a"],
            "status": "retired",
            "details": "test launchsite with launch",
            "id": "5e9e4501f5090910d4566f83",
        },
        {
            "images": {"large": ["https://i.imgur.com/7uXe1Kv.png"]},
            "name": "other",
            "full_name": "test name",
            "locality": "test Force Base",
            "region": "somewhere",
            "latitude": 34.6440904,
            "longitude": -120.5931438,
            "launch_attempts": 0,
            "launch_successes": 0,
            "rockets": ["5e9d0d95eda69955f709d1eb"],
            "timezone": "sometimezone",
            "launches": [],
            "status": "retired",
            "details": "somedetails",
            "id": "test_id_2",
        },
    ]


@pytest.fixture
def example_launches(example_launch_json):
    return [Launch(**launch) for launch in example_launch_json]


@pytest.fixture
def example_launchpads(example_launchpad_json):
    return [Launchpad(**launchpad) for launchpad in example_launchpad_json]


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
