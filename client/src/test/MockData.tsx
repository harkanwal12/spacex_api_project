function mockLaunchesLoader() {
    return [
        {
            "date_utc": "Fri, 24 Mar 2006 22:30:00 GMT",
            "id": "5eb87cd9ffd86e000604b32a",
            "name": "FalconSat",
            "success": false,
        },
        {
            "date_utc": "Wed, 21 Mar 2007 01:10:00 GMT",
            "id": "5eb87cdaffd86e000604b32b",
            "name": "DemoSat",
            "success": false,
        },
    ]
}

function mockLaunchpadsAndLaunchesLoader() {
    return [
        {
            "details": "test launchsite with launch",
            "full_name": "Vandenberg Space Force Base Space Launch Complex 3W",
            "id_launchpad": "5e9e4501f5090910d4566f83",
            "images": "https://i.imgur.com/7uXe1Kv.png",
            "launch_attempts": 0,
            "launches": [
                {
                    "date_utc": "Fri, 24 Mar 2006 22:30:00 GMT",
                    "id_launch": "5eb87cd9ffd86e000604b32a",
                    "name_launch": "FalconSat",
                    "success": false,
                }
            ],
            "locality": "Vandenberg Space Force Base",
            "name_launchpad": "VAFB SLC 3W",
            "status": "retired",
        },
        {
            "details": "somedetails",
            "full_name": "test name",
            "id_launchpad": "test_id_2",
            "images": "https://i.imgur.com/7uXe1Kv.png",
            "launch_attempts": 0,
            "launches": [],
            "locality": "test Force Base",
            "name_launchpad": "other",
            "status": "retired",
        },
    ]
}

export { mockLaunchesLoader, mockLaunchpadsAndLaunchesLoader };