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

const mockLaunchSitesWithLaunches = [
    {
        details: "SpaceX's primary Falcon 9 pad, where all east coast Falcon 9s launched prior to the AMOS-6 anomaly. Previously used alongside SLC-41 to launch Titan rockets for the US Air Force, the pad was heavily damaged by the AMOS-6 anomaly in September 2016. It returned to flight with CRS-13 on December 15, 2017, boasting an upgraded throwback-style Transporter-Erector modeled after that at LC-39A.",
        full_name: "Cape Canaveral Space Force Station Space Launch Complex 40",
        id: "5e9e4501f509094ba4566f84",
        images: "https://i.imgur.com/9oEMXwa.png",
        latitude: 28.5618571,
        launch_attempts: 99,
        launch_success_rate: "98%",
        launch_successes: 97,
        launches: [
            {
            auto_update: true,
            capsules: [
            ],
            cores: [
              {
                core: "5e9e28a6f359183c413b265d",
                flight: 7,
                gridfins: true,
                landing_attempt: true,
                landing_success: true,
                landing_type: "ASDS",
                landpad: "5e9e3033383ecbb9e534e7cc",
                legs: true,
                reused: true,
              },
            ],
            crew: [
            ],
            date_local: "2022-09-04T22:09:00-04:00",
            date_precision: "hour",
            date_unix: 1662343740,
            date_utc: "2022-09-05T02:09:00.000Z",
            details: null,
            failures: [
            ],
            fairings: {
              recovered: null,
              recovery_attempt: null,
              reused: null,
              ships: [
              ],
            },
            flight_number: 183,
            id: "62f3b5330f55c50e192a4e6e",
            launch_library_id: null,
            launchpad: "5e9e4501f509094ba4566f84",
            links: {
              article: null,
              flickr: {
                original: [
                ],
                small: [
                ],
              },
              patch: {
                large: "https://images2.imgbox.com/57/42/trORYoRc_o.png",
                small: "https://images2.imgbox.com/dc/a0/erKL6HGq_o.png",
              },
              presskit: null,
              reddit: {
                campaign: "https://www.reddit.com/r/spacex/comments/jhu37i/starlink_general_discussion_and_deployment_thread/",
                launch: null,
                media: null,
                recovery: "https://www.reddit.com/r/spacex/comments/k2ts1q/rspacex_fleet_updates_discussion_thread/",
              },
              webcast: "https://youtu.be/NONM-xsKMSs",
              wikipedia: null,
              youtube_id: "NONM-xsKMSs",
            },
            name: "Starlink 4-20 (v1.5) & Sherpa LTC-2/Varuna-TDM",
            net: false,
            payloads: [
              "631614e9ffc78f3b85670717",
              "631617fbffc78f3b8567071d",
            ],
            rocket: "5e9d0d95eda69973a809d1ec",
            ships: [
            ],
            static_fire_date_unix: null,
            static_fire_date_utc: null,
            success: false,
            tbd: false,
            upcoming: false,
            window: null,
          },
          {
            auto_update: true,
            capsules: [
            ],
            cores: [
              {
                core: "60b800111f83cc1e59f16438",
                flight: 6,
                gridfins: true,
                landing_attempt: true,
                landing_success: true,
                landing_type: "ASDS",
                landpad: "5e9e3033383ecbb9e534e7cc",
                legs: true,
                reused: true,
              },
            ],
            crew: [
            ],
            date_local: "2022-09-16T21:05:00-04:00",
            date_precision: "hour",
            date_unix: 1663376700,
            date_utc: null,
            details: null,
            failures: [
            ],
            fairings: {
              recovered: null,
              recovery_attempt: null,
              reused: null,
              ships: [
              ],
            },
            flight_number: 185,
            id: "63161329ffc78f3b8567070b",
            launch_library_id: "9ba04064-c329-40bf-b477-ff468d7d8058",
            launchpad: "5e9e4501f509094ba4566f84",
            links: {
              article: null,
              flickr: {
                original: [
                ],
                small: [
                ],
              },
              patch: {
                large: "https://images2.imgbox.com/e3/cc/hN96PmST_o.png",
                small: "https://images2.imgbox.com/a9/9a/NXVkTZCE_o.png",
              },
              presskit: null,
              reddit: {
                campaign: "https://www.reddit.com/r/spacex/comments/jhu37i/starlink_general_discussion_and_deployment_thread/",
                launch: "https://www.reddit.com/r/spacex/comments/xd8vhj/rspacex_starlink_434_launch_discussion_and/",
                media: null,
                recovery: "https://www.reddit.com/r/spacex/comments/k2ts1q/rspacex_fleet_updates_discussion_thread/",
              },
              webcast: "https://youtu.be/ZlQHF_yBkMQ",
              wikipedia: null,
              youtube_id: "ZlQHF_yBkMQ",
            },
            name: "Starlink 4-34 (v1.5)",
            net: false,
            payloads: [
              "63161699ffc78f3b85670719",
            ],
            rocket: "5e9d0d95eda69973a809d1ec",
            ships: [
            ],
            static_fire_date_unix: null,
            static_fire_date_utc: null,
            success: null,
            tbd: false,
            upcoming: false,
            window: null,
          },
          {
            auto_update: true,
            capsules: [
            ],
            cores: [
              {
                core: "627843d657b51b752c5c5a53",
                flight: 4,
                gridfins: true,
                landing_attempt: true,
                landing_success: true,
                landing_type: "ASDS",
                landpad: "5e9e3033383ecbb9e534e7cc",
                legs: true,
                reused: true,
              },
            ],
            crew: [
            ],
            date_local: "2022-09-24T19:30:00-04:00",
            date_precision: "hour",
            date_unix: 1664062200,
            date_utc: "2022-09-24T23:30:00.000Z",
            details: null,
            failures: [
            ],
            fairings: {
              recovered: null,
              recovery_attempt: null,
              reused: null,
              ships: [
              ],
            },
            flight_number: 186,
            id: "63161339ffc78f3b8567070c",
            launch_library_id: "1c903b65-6667-4fd5-944d-296c5f13e01f",
            launchpad: "5e9e4501f509094ba4566f84",
            links: {
              article: null,
              flickr: {
                original: [
                ],
                small: [
                ],
              },
              patch: {
                large: "https://images2.imgbox.com/e3/cc/hN96PmST_o.png",
                small: "https://images2.imgbox.com/a9/9a/NXVkTZCE_o.png",
              },
              presskit: null,
              reddit: {
                campaign: "https://www.reddit.com/r/spacex/comments/jhu37i/starlink_general_discussion_and_deployment_thread/",
                launch: "https://www.reddit.com/r/spacex/comments/xn028t/rspacex_starlink_435_launch_discussion_and/",
                media: null,
                recovery: "https://www.reddit.com/r/spacex/comments/k2ts1q/rspacex_fleet_updates_discussion_thread/",
              },
              webcast: "https://youtu.be/VVu2bSJJhgI",
              wikipedia: null,
              youtube_id: "VVu2bSJJhgI",
            },
            name: "Starlink 4-35 (v1.5)",
            net: false,
            payloads: [
              "631616a7ffc78f3b8567071a",
            ],
            rocket: "5e9d0d95eda69973a809d1ec",
            ships: [
            ],
            static_fire_date_unix: null,
            static_fire_date_utc: null,
            success: true,
            tbd: false,
            upcoming: false,
            window: null,
          },
        ],
        locality: "Cape Canaveral",
        longitude: -80.577366,
        name: "CCSFS SLC 40",
        region: "Florida",
        status: "active",
      }
]

const mockLaunchSitesWithNoLaunches = [
  {
      details: "SpaceX's primary Falcon 9 pad, where all east coast Falcon 9s launched prior to the AMOS-6 anomaly. Previously used alongside SLC-41 to launch Titan rockets for the US Air Force, the pad was heavily damaged by the AMOS-6 anomaly in September 2016. It returned to flight with CRS-13 on December 15, 2017, boasting an upgraded throwback-style Transporter-Erector modeled after that at LC-39A.",
      full_name: "Cape Canaveral Space Force Station Space Launch Complex 40",
      id: "5e9e4501f509094ba4566f84",
      images: "https://i.imgur.com/9oEMXwa.png",
      latitude: 28.5618571,
      launch_attempts: 99,
      launch_success_rate: "98%",
      launch_successes: 97,
      launches: [],
      locality: "Cape Canaveral",
      longitude: -80.577366,
      name: "CCSFS SLC 40",
      region: "Florida",
      status: "active",
    }
]

function mockLaunchSitesLoader() {
    return [
        {
            full_name: "Vandenberg Space Force Base Space Launch Complex 3W",
            id: "5e9e4501f5090910d4566f83",
            name: "VAFB SLC 3W",
        },
        {
            full_name: "Cape Canaveral Space Force Station Space Launch Complex 40",
            id: "5e9e4501f509094ba4566f84",
            name: "CCSFS SLC 40",
        }
    ]
}

export { mockLaunchesInYear, mockLaunchSitesWithNoLaunches, mockLaunchSitesWithLaunches, mockLaunchesLoader, mockLaunchSitesLoader };