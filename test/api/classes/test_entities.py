from api.classes.entities import Launch, Launchpad


def test_create_launch_entity(example_launch_json):
    launch = Launch(**example_launch_json[0])
    assert isinstance(launch, Launch)


def test_create_launch_entity_required_args_only():
    launch = Launch(id="someid")
    assert isinstance(launch, Launch)


def test_create_launchpad_entity(example_launchpad_json):
    launch = Launchpad(**example_launchpad_json[0])
    assert isinstance(launch, Launchpad)


def test_create_launchpad_entity_required_args_only():
    launch = Launchpad(id="someid")
    assert isinstance(launch, Launchpad)
