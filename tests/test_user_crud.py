import pytest
import requests
from assertpy import assert_that, soft_assertions
from client.user_client import UserClient
from jsonschema import validate

from config import PASSWORD, USERNAME
from utils.file_reader import get_schema_from_template


@pytest.fixture(scope="session")
def user_client() -> UserClient:
    return UserClient()


@pytest.fixture
def get_user(user_client: UserClient) -> requests.Response:
    return user_client.get_user("User Name").json()


def test_create_user(user_client: UserClient):
    response = user_client.create_user(USERNAME, PASSWORD)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()).is_not_empty().contains("name")
        assert_that(response.json()["name"]).is_equal_to("User Name")
        assert_that(validate(response.json(),
                             get_schema_from_template("schema_user_created.json")))


def test_get_user_by_id(get_user: requests.Response):
    response = get_user
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json).is_not_empty()


def test_update_user_first_name(get_user: requests.Response, user_client: UserClient):
    user_id = get_user.json()["name"]
    response = user_client.update_user(user_id, PASSWORD, first_name="New")
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()).is_not_empty()
        assert_that(response.json()["first_name"]).is_equal_to("New")


def test_delete_user(user_client: UserClient, get_user: requests.Response):
    user_id = get_user.json()["name"]
    response = user_client.delete_user(user_name=USERNAME)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.json()).is_not_empty()
        assert_that(response.json()["users"]).is_equal_to(user_id)
        assert_that(validate(response.json(), get_schema_from_template("schema_user_deleted.json")))


def test_get_all_users(user_client: UserClient):
    response = user_client.get_users()
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()).is_not_empty()
