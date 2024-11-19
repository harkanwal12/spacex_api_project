function mockLaunchesLoader() {
    return [2001, 2002, 2003, 2022, 2005]
}

const mockLaunchesInYear = [
    {
        date_utc: "Mon, 08 Jan 2018 01:00:00 GMT",
        details: "Originally planned for mid-November 2017, the mission was delayed due to test results from the fairing of another customer. First-stage booster will attempt landing at LZ-1",
        id: "5eb87d10ffd86e000604b35e",
        name: "ZUMA",
        patch: null,
        reddit: null,
        success: null,
        webcast: null,
        wikipedia: null,
    },
    {
        date_utc: "Wed, 31 Jan 2018 21:25:00 GMT",
        details: "Reused booster from the classified NROL-76 mission in May 2017. Following a successful experimental ocean landing that used three engines, the booster unexpectedly remained intact; Elon Musk stated in a tweet that SpaceX will attempt to tow the booster to shore.",
        id: "5eb87d11ffd86e000604b35f",
        name: "SES-16 / GovSat-1",
        patch: "https://images2.imgbox.com/e0/b5/G8QLLURl_o.png",
        reddit: null,
        success: true,
        webcast: "https://www.youtube.com/watch?v=ScYUA51-POQ",
        wikipedia: "https://en.wikipedia.org/wiki/List_of_SES_satellites#SES_Fleet",
    },
    {
        date_utc: "Tue, 06 Feb 2012 20:45:00 GMT",
        details: "The launch was a success, and the side boosters landed simultaneously at adjacent ground pads. Drone ship landing of the central core failed. Final burn to heliocentric mars-earth orbit was successful after the second stage and payload passed through the Van Allen belts.",
        id: "5eb87d13ffd86e000604b360",
        name: "Falcon Heavy Test Flight",
        patch: "https://images2.imgbox.com/cd/48/NVrODg2G_o.png",
        reddit: "enabledlink",
        success: false,
        webcast: "https://www.youtube.com/watch?v=wbSwFU6tY1c",
        wikipedia: "https://en.wikipedia.org/wiki/Elon_Musk%27s_Tesla_Roadster",
    }
]

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
            "images": "some other link",
            "launch_attempts": 0,
            "launches": [],
            "locality": "test Force Base",
            "name_launchpad": "other",
            "status": "retired",
        },
    ]
}

export { mockLaunchesInYear, mockLaunchesLoader, mockLaunchpadsAndLaunchesLoader };