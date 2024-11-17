from api.classes.entities import Launch, Launchpad


def test_create_launch_entity(example_launch_json):
    launch = Launch(**example_launch_json[0])
    assert isinstance(launch, Launch)


def test_create_launch_entity_required_args_only():
    launch = Launch(
        id="someid", name="somename", date_utc="somedate", launchpad="somesite"
    )
    assert isinstance(launch, Launch)


def test_create_launchpad_entity(example_launchpad_json):
    launch = Launchpad(**example_launchpad_json[0])
    assert isinstance(launch, Launchpad)


def test_create_launchpad_entity_required_args_only():
    launch = Launchpad(
        id="someid",
        name="somename",
        full_name="somename",
        locality="someplace",
        status="somestatus",
        images="someimage",
        details="somedetails",
        launches="somelaunches",
    )
    assert isinstance(launch, Launchpad)
