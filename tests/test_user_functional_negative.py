import pytest


@pytest.fixture
def new_user():
    pass


@pytest.fixture()
def del_user():
    pass


def test_create_user_with_duplicate_name():
    pass


def test_create_user_with_existing_email():
    pass


def test_create_user_missing_required_fields():
    pass


def test_create_user_with_invalid_email():
    pass


def test_create_user_with_invalid_json():
    pass


def test_update_nonexistent_user():
    pass


def test_update_user_without_authentication():
    pass


# here should be a bunch of tests
# as example we can use DDT approach for <name> fild only
@pytest.mark.parametrize("invalid_data",
                         [
                             {"name": ""},  # empty
                             {"name": "a" * 512},  # too long
                             {"name": "NULL"},  # NULL
                             {"name": "NaN"},  # NaN
                             {"name": "TRUE"},  # boolean
                             {"name": "int"},  # primitive
                             {"name": "ооиоыаиыо"}  # non latin symbols
                         ])
def test_update_user_with_invalid_parameters():
    pass


def test_delete_nonexistent_user():
    pass


def test_get_user_by_invalid_id():
    pass
