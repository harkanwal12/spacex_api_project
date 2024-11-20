from api.classes.exceptions import NoDataFoundException
from werkzeug.exceptions import Unauthorized
from api.routes import success_rate_calculator
import numpy as np


def test_get_api_home(mock_app):
    response = mock_app.test_client().get("/api/")

    assert response.status_code == 200
    assert response.json == "Welcome to the SpaceX Python Wrapper API"


def test_get_all_launch_years_success(mock_app, example_launch_years):
    mock_app.spacex_api.get_launches.return_value = example_launch_years
    response = mock_app.test_client().get("/api/get_all_launch_years")

    expected_response = [2007, 2003, 2009]

    expected_query = {
        "query": {},
        "options": {
            "pagination": False,
            "select": {"date_utc": 1, "id": 1},
        },
    }

    assert response.status_code == 200
    assert response.json == expected_response
    mock_app.spacex_api.get_launches.assert_called_with(query=expected_query)


def test_get_all_launch_years_error_404(mock_app):
    mock_app.spacex_api.get_launches.side_effect = NoDataFoundException

    response = mock_app.test_client().get("/api/get_all_launch_years")

    assert response.status_code == 404
    assert response.json == "No data was found"


def test_get_all_launch_years_unknown_exception(mock_app):
    mock_app.spacex_api.get_launches.side_effect = Exception

    response = mock_app.test_client().get("/api/get_all_launch_years")

    assert response.status_code == 500
    assert (
        response.json
        == "Unknown error occurred, please contact API developers for assistance"
    )


def test_get_all_launch_years_with_http_exception(mock_app):
    mock_app.spacex_api.get_launches.side_effect = Unauthorized

    response = mock_app.test_client().get("/api/get_all_launch_years")

    assert response.status_code == 401
    assert response.json["name"] == "Unauthorized"


def test_get_all_launches_in_year(mock_app, example_launches):
    mock_app.spacex_api.get_launches.return_value = example_launches
    response = mock_app.test_client().get("/api/2010/get_all_launches_in_year")

    expected_query = {
        "query": {
            "date_utc": {
                "$gte": "2010-01-01 00:00:00",
                "$lt": "2011-01-01 00:00:00",
            }
        },
        "options": {
            "pagination": False,
        },
    }

    expected_response = [
        {
            "date_utc": "Fri, 24 Mar 2006 22:30:00 GMT",
            "details": "Engine failure at 33 seconds and loss of vehicle",
            "id": "5eb87cd9ffd86e000604b32a",
            "name": "FalconSat",
            "patch": "https://images2.imgbox.com/94/f2/NN6Ph45r_o.png",
            "reddit": "null",
            "success": False,
            "webcast": "https://www.youtube.com/watch?v=0a_00nJ_Y88",
            "wikipedia": "https://en.wikipedia.org/wiki/DemoSat",
        },
        {
            "date_utc": "Wed, 21 Mar 2007 01:10:00 GMT",
            "details": "Successful first stage burn and transition to second stage, maximum altitude 289 km, Premature engine shutdown at T+7 min 30 s, Failed to reach orbit, Failed to recover first stage",
            "id": "5eb87cdaffd86e000604b32b",
            "name": "DemoSat",
            "patch": "https://images2.imgbox.com/f9/4a/ZboXReNb_o.png",
            "reddit": "null",
            "success": False,
            "webcast": "https://www.youtube.com/watch?v=Lk4zQ2wP-Nc",
            "wikipedia": "https://en.wikipedia.org/wiki/DemoSat",
        },
    ]

    assert response.status_code == 200
    assert response.json == expected_response
    mock_app.spacex_api.get_launches.assert_called_with(query=expected_query)


def test_get_all_launches_in_year_error_404(mock_app):
    mock_app.spacex_api.get_launches.side_effect = NoDataFoundException

    response = mock_app.test_client().get("/api/2022/get_all_launches_in_year")

    assert response.status_code == 404
    assert response.json == "No data was found"


def test_get_all_launchpad_names_success(mock_app, example_launchpad_names):
    mock_app.spacex_api.get_launchpads.return_value = example_launchpad_names
    response = mock_app.test_client().get("/api/get_all_launchpad_names")

    expected_response = [
        {
            "full_name": "Vandenberg Space Force Base Space Launch Complex 3W",
            "id": "5e9e4501f5090910d4566f83",
            "name": "VAFB SLC 3W",
        },
        {"full_name": "test name", "id": "test_id_2", "name": "other"},
    ]

    expected_query = {
        "query": {},
        "options": {
            "pagination": False,
            "select": {"id": 1, "name": 1, "full_name": 1},
        },
    }

    assert response.status_code == 200
    assert response.json == expected_response
    mock_app.spacex_api.get_launchpads.assert_called_with(query=expected_query)


def test_get_all_launchpad_names_error_404(mock_app):
    mock_app.spacex_api.get_launchpads.side_effect = NoDataFoundException

    response = mock_app.test_client().get("/api/get_all_launchpad_names")

    assert response.status_code == 404
    assert response.json == "No data was found"


def test_get_launchpad_with_launches_success(
    mock_app, example_launchpad_with_launches
):
    mock_app.spacex_api.get_launchpads.return_value = (
        example_launchpad_with_launches
    )
    response = mock_app.test_client().get(
        "api/someid/someshortname/get_launchpad_with_launches"
    )

    expected_query = {
        "query": {
            "id": {"$eq": "someid"},
            "name": {"$eq": "someshortname"},
        },
        "options": {
            "populate": ["launches"],
            "pagination": False,
            "select": {
                "rockets": 0,
                "timezone": 0,
            },
        },
    }

    expected_response = [
        {
            "details": "NASA's historic pad that launched most of the Saturn V and Space Shuttle missions, including Apollo 11. SpaceX initially leased solely for Falcon Heavy and Crew Dragon launches, but the company has also used it for others as well following the damage to SLC-40 in the AMOS-6 explosion. After completing the necessary modifications, the first launch SpaceX performed on the pad was CRS-10 in February 2017. After SLC-40 was back online, 39A was upgraded to support Falcon Heavy and complete the removal of the shuttle-era Rotating Service Structure. More recently, a crew access arm and other safety equipment has been installed in order to launch commercial crew missions. 39A also occasionally launches other Falcon 9 missions between Falcon Heavy and Crew Dragon launches, depending on pad scheduling. The pad may also potentially be upgraded in the future for use with the BFR.",
            "full_name": "Kennedy Space Center Historic Launch Complex 39A",
            "id": "5e9e4502f509094188566f88",
            "images": "https://i.imgur.com/1jwU0Pk.png",
            "latitude": 28.6080585,
            "launch_attempts": 55,
            "launch_success_rate": "100%",
            "launch_successes": 55,
            "launches": [
                {
                    "auto_update": True,
                    "capsules": ["5e9e2c5cf359185d753b266f"],
                    "cores": None,
                    "crew": [],
                    "date_local": "2017-02-19T10:39:00-04:00",
                    "date_precision": "hour",
                    "date_unix": 1487515140,
                    "date_utc": "2017-02-19T14:39:00.000Z",
                    "details": "First Falcon 9 flight from the historic LC-39A launchpad at Kennedy Space Center, carrying supplies and materials to support dozens of science and research investigations scheduled during ISS Expeditions 50 and 51. The first stage returned to launch site and landed at LZ-1.",
                    "failures": [],
                    "fairings": None,
                    "flight_number": 36,
                    "id": "5eb87cfeffd86e000604b34d",
                    "launch_library_id": None,
                    "launchpad": "5e9e4502f509094188566f88",
                    "links": {
                        "article": "https://spaceflightnow.com/2017/02/19/historic-launch-pad-back-in-service-with-thundering-blastoff-by-spacex/",
                        "flickr": None,
                        "patch": {
                            "small": "https://images2.imgbox.com/56/9d/gvzAqLFg_o.png",
                            "large": "https://images2.imgbox.com/52/a0/z8Dwflcz_o.png",
                        },
                        "presskit": "http://www.spacex.com/sites/spacex/files/crs10presskitfinal.pdf",
                        "reddit": {
                            "campaign": "https://www.reddit.com/r/spacex/comments/5n2e10/echostar_23_launch_campaign_thread/",
                            "launch": "https://www.reddit.com/r/spacex/comments/5z8dkm/welcome_to_the_rspacex_echostar23_official_launch/",
                            "media": "https://www.reddit.com/r/spacex/comments/5z8if6/rspacex_echostar_23_media_thread_videos_images/",
                            "recovery": None,
                        },
                        "webcast": "https://www.youtube.com/watch?v=giNhaEzv_PI",
                        "wikipedia": "https://en.wikipedia.org/wiki/SpaceX_CRS-10",
                        "youtube_id": "giNhaEzv_PI",
                    },
                    "name": "CRS-10",
                    "net": False,
                    "payloads": ["5eb0e4c3b6c3bb0006eeb209"],
                    "rocket": "5e9d0d95eda69973a809d1ec",
                    "ships": ["5ea6ed30080df4000697c912"],
                    "static_fire_date_unix": 1486935000,
                    "static_fire_date_utc": "2017-02-12T21:30:00.000Z",
                    "success": True,
                    "tbd": False,
                    "upcoming": False,
                    "window": 0,
                },
                {
                    "auto_update": True,
                    "capsules": [],
                    "cores": None,
                    "crew": [],
                    "date_local": "2017-03-16T02:00:00-04:00",
                    "date_precision": "hour",
                    "date_unix": 1489644000,
                    "date_utc": "2017-03-16T06:00:00.000Z",
                    "details": "Communications satellite for EchoStar Corp. EchoStar XXIII, based on a spare platform from the cancelled CMBStar 1 satellite program, will provide direct-to-home television broadcast services over Brazil. There was no attempt at a first-stage recovery so this rocket did not have landing legs or grid fins.",
                    "failures": [],
                    "fairings": {
                        "recovered": False,
                        "recovery_attempt": False,
                        "reused": False,
                        "ships": None,
                    },
                    "flight_number": 37,
                    "id": "5eb87cfeffd86e000604b34e",
                    "launch_library_id": None,
                    "launchpad": "5e9e4502f509094188566f88",
                    "links": {
                        "article": "http://spacenews.com/spacex-launches-echostar-23/",
                        "flickr": None,
                        "patch": {
                            "small": "https://images2.imgbox.com/11/eb/qqrhHFhv_o.png",
                            "large": "https://images2.imgbox.com/ea/43/D4tA0WaM_o.png",
                        },
                        "presskit": "http://www.spacex.com/sites/spacex/files/echostarxxiiifinal.pdf",
                        "reddit": {
                            "campaign": "https://www.reddit.com/r/spacex/comments/5n2eqx",
                            "launch": "https://www.reddit.com/r/spacex/comments/5uw4bh",
                            "media": "https://www.reddit.com/r/spacex/comments/5uoy8o",
                            "recovery": "https://www.reddit.com/r/spacex/comments/609aq4",
                        },
                        "webcast": "https://www.youtube.com/watch?v=lZmqbL-hz7U",
                        "wikipedia": "https://en.wikipedia.org/wiki/EchoStar#Satellite_fleet",
                        "youtube_id": "lZmqbL-hz7U",
                    },
                    "name": "EchoStar 23",
                    "net": False,
                    "payloads": ["5eb0e4c3b6c3bb0006eeb20a"],
                    "rocket": "5e9d0d95eda69973a809d1ec",
                    "ships": [],
                    "static_fire_date_unix": 1489100400,
                    "static_fire_date_utc": "2017-03-09T23:00:00.000Z",
                    "success": True,
                    "tbd": False,
                    "upcoming": False,
                    "window": 9000,
                },
            ],
            "locality": "Cape Canaveral",
            "longitude": -80.6039558,
            "name": "KSC LC 39A",
            "region": "Florida",
            "status": "active",
        }
    ]

    assert response.status_code == 200
    assert response.json == expected_response
    mock_app.spacex_api.get_launchpads.assert_called_with(query=expected_query)


def test_get_launchpad_with_launches_error_404(mock_app):
    mock_app.spacex_api.get_launchpads.side_effect = NoDataFoundException

    response = mock_app.test_client().get(
        "/api/someid/somename/get_launchpad_with_launches"
    )

    assert response.status_code == 404
    assert response.json == "No data was found"


def test_success_rate_calculator():
    assert success_rate_calculator(attempts=0, successes=0) == "N/A"
    assert success_rate_calculator(attempts=None, successes=0) == "N/A"
    assert success_rate_calculator(attempts=None, successes=None) == "N/A"
    assert success_rate_calculator(attempts=21, successes=0) == "0%"
    assert success_rate_calculator(attempts=0, successes=21) == "N/A"
    assert success_rate_calculator(attempts=121, successes=131) == "108%"
    assert success_rate_calculator(attempts=np.nan, successes=131) == "N/A"
    assert success_rate_calculator(attempts=np.nan, successes=np.nan) == "N/A"
