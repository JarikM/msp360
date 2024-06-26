import pytest


@pytest.fixture
def new_user():
    pass


@pytest.fixture()
def del_user():
    pass


def test_update_user_name(new_user, del_user):
    pass


def test_update_user_password(new_user, del_user):
    pass


# here should be a bunch of tests
# as example we can use DDT approach for <name> fild only
@pytest.mark.parametrize("valid_name_options",
                         [
                             {"name": "a"},  # minimal number
                             {"name": "a" * 256},  # maximum number
                             {"name": "AbCd"},  # camel case
                             {"name": "A B C D"},  # use spaces
                         ])
def test_update_user_some_field(new_user, del_user, valid_name_options):
    pass


# if pagination is available when getting list of all users
def test_get_users_pagination():
    pass
