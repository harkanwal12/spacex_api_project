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
def example_launchpad_with_launches():
    data = {
        "images": {"large": ["https://i.imgur.com/1jwU0Pk.png"]},
        "name": "KSC LC 39A",
        "full_name": "Kennedy Space Center Historic Launch Complex 39A",
        "locality": "Cape Canaveral",
        "region": "Florida",
        "latitude": 28.6080585,
        "longitude": -80.6039558,
        "launch_attempts": 55,
        "launch_successes": 55,
        "launches": [
            {
                "fairings": None,
                "links": {
                    "patch": {
                        "small": "https://images2.imgbox.com/56/9d/gvzAqLFg_o.png",
                        "large": "https://images2.imgbox.com/52/a0/z8Dwflcz_o.png",
                    },
                    "reddit": {
                        "campaign": "https://www.reddit.com/r/spacex/comments/5n2e10/echostar_23_launch_campaign_thread/",
                        "launch": "https://www.reddit.com/r/spacex/comments/5z8dkm/welcome_to_the_rspacex_echostar23_official_launch/",
                        "media": "https://www.reddit.com/r/spacex/comments/5z8if6/rspacex_echostar_23_media_thread_videos_images/",
                        "recovery": None,
                    },
                    "flickr": None,
                    "presskit": "http://www.spacex.com/sites/spacex/files/crs10presskitfinal.pdf",
                    "webcast": "https://www.youtube.com/watch?v=giNhaEzv_PI",
                    "youtube_id": "giNhaEzv_PI",
                    "article": "https://spaceflightnow.com/2017/02/19/historic-launch-pad-back-in-service-with-thundering-blastoff-by-spacex/",
                    "wikipedia": "https://en.wikipedia.org/wiki/SpaceX_CRS-10",
                },
                "static_fire_date_utc": "2017-02-12T21:30:00.000Z",
                "static_fire_date_unix": 1486935000,
                "net": False,
                "window": 0,
                "rocket": "5e9d0d95eda69973a809d1ec",
                "success": True,
                "failures": [],
                "details": "First Falcon 9 flight from the historic LC-39A launchpad at Kennedy Space Center, carrying supplies and materials to support dozens of science and research investigations scheduled during ISS Expeditions 50 and 51. The first stage returned to launch site and landed at LZ-1.",
                "crew": [],
                "ships": ["5ea6ed30080df4000697c912"],
                "capsules": ["5e9e2c5cf359185d753b266f"],
                "payloads": ["5eb0e4c3b6c3bb0006eeb209"],
                "launchpad": "5e9e4502f509094188566f88",
                "flight_number": 36,
                "name": "CRS-10",
                "date_utc": "2017-02-19T14:39:00.000Z",
                "date_unix": 1487515140,
                "date_local": "2017-02-19T10:39:00-04:00",
                "date_precision": "hour",
                "upcoming": False,
                "cores": None,
                "auto_update": True,
                "tbd": False,
                "launch_library_id": None,
                "id": "5eb87cfeffd86e000604b34d",
            },
            {
                "fairings": {
                    "reused": False,
                    "recovery_attempt": False,
                    "recovered": False,
                    "ships": None,
                },
                "links": {
                    "patch": {
                        "small": "https://images2.imgbox.com/11/eb/qqrhHFhv_o.png",
                        "large": "https://images2.imgbox.com/ea/43/D4tA0WaM_o.png",
                    },
                    "reddit": {
                        "campaign": "https://www.reddit.com/r/spacex/comments/5n2eqx",
                        "launch": "https://www.reddit.com/r/spacex/comments/5uw4bh",
                        "media": "https://www.reddit.com/r/spacex/comments/5uoy8o",
                        "recovery": "https://www.reddit.com/r/spacex/comments/609aq4",
                    },
                    "flickr": None,
                    "presskit": "http://www.spacex.com/sites/spacex/files/echostarxxiiifinal.pdf",
                    "webcast": "https://www.youtube.com/watch?v=lZmqbL-hz7U",
                    "youtube_id": "lZmqbL-hz7U",
                    "article": "http://spacenews.com/spacex-launches-echostar-23/",
                    "wikipedia": "https://en.wikipedia.org/wiki/EchoStar#Satellite_fleet",
                },
                "static_fire_date_utc": "2017-03-09T23:00:00.000Z",
                "static_fire_date_unix": 1489100400,
                "net": False,
                "window": 9000,
                "rocket": "5e9d0d95eda69973a809d1ec",
                "success": True,
                "failures": [],
                "details": "Communications satellite for EchoStar Corp. EchoStar XXIII, based on a spare platform from the cancelled CMBStar 1 satellite program, will provide direct-to-home television broadcast services over Brazil. There was no attempt at a first-stage recovery so this rocket did not have landing legs or grid fins.",
                "crew": [],
                "ships": [],
                "capsules": [],
                "payloads": ["5eb0e4c3b6c3bb0006eeb20a"],
                "launchpad": "5e9e4502f509094188566f88",
                "flight_number": 37,
                "name": "EchoStar 23",
                "date_utc": "2017-03-16T06:00:00.000Z",
                "date_unix": 1489644000,
                "date_local": "2017-03-16T02:00:00-04:00",
                "date_precision": "hour",
                "upcoming": False,
                "cores": None,
                "auto_update": True,
                "tbd": False,
                "launch_library_id": None,
                "id": "5eb87cfeffd86e000604b34e",
            },
        ],
        "status": "active",
        "details": "NASA's historic pad that launched most of the Saturn V and Space Shuttle missions, including Apollo 11. SpaceX initially leased solely for Falcon Heavy and Crew Dragon launches, but the company has also used it for others as well following the damage to SLC-40 in the AMOS-6 explosion. After completing the necessary modifications, the first launch SpaceX performed on the pad was CRS-10 in February 2017. After SLC-40 was back online, 39A was upgraded to support Falcon Heavy and complete the removal of the shuttle-era Rotating Service Structure. More recently, a crew access arm and other safety equipment has been installed in order to launch commercial crew missions. 39A also occasionally launches other Falcon 9 missions between Falcon Heavy and Crew Dragon launches, depending on pad scheduling. The pad may also potentially be upgraded in the future for use with the BFR.",
        "id": "5e9e4502f509094188566f88",
    }
    return [Launchpad(**data)]


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
def example_launch_years():
    launch_years = [
        {"id": "someid1", "date_utc": "2007-03-21T01:10:00.000Z"},
        {"id": "someid2", "date_utc": "2003-03-21T01:10:00.000Z"},
        {"id": "someid3", "date_utc": "2003-07-26T01:10:00.000Z"},
        {"id": "someid4", "date_utc": "2009-07-26T01:11:22.230Z"},
    ]
    return [Launch(**launch) for launch in launch_years]


@pytest.fixture
def example_launchpad_names():
    launchpad_names = [
        {
            "name": "VAFB SLC 3W",
            "full_name": "Vandenberg Space Force Base Space Launch Complex 3W",
            "id": "5e9e4501f5090910d4566f83",
        },
        {
            "name": "other",
            "full_name": "test name",
            "id": "test_id_2",
        },
    ]
    return [Launchpad(**launchpad) for launchpad in launchpad_names]


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
