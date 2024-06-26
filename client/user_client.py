from typing import Optional

import requests

from client.base_client import BaseClient
from config import BASE_URI


class UserClient(BaseClient):
    def __init__(self) -> None:
        super().__init__()

    def create_user(self, name: str, password: str, first_name: Optional[str] = None,
                    last_name: Optional[str] = None, company_id: Optional[int] = None,
                    notification_emails: Optional[list] = None, enabled: Optional[bool] = None,
                    user_destinations: Optional[list] = None, licensing_mode: Optional[int] = None,
                    licenses_granted: Optional[list] = None) -> requests.Response:
        json_body = {
            "name": name,
            "password": password,
            "firstName": first_name,
            "lastName": last_name,
            "companyId": company_id,
            "notificationEmails": notification_emails,
            "enabled": enabled,
            "userDestinations": user_destinations,
            "licensingMode": licensing_mode,
            "licensesGranted": licenses_granted
        }
        return self._session.post(BASE_URI, json=json_body)

    def delete_user(self, user_name: str) -> requests.Response:
        url = f"{BASE_URI}/{user_name}"
        return self._session.delete(url)

    def get_user(self, user_name: str) -> requests.Response:
        url = f"{BASE_URI}/{user_name}"
        return self._session.get(url)

    def get_users(self) -> requests.Response:
        url = f"{BASE_URI}"
        return self._session.get(url)

    def update_user(self, name: str, password: str, first_name: Optional[str] = None,
                    last_name: Optional[str] = None, company_id: Optional[int] = None,
                    notification_emails: Optional[list] = None, enabled: bool = None,
                    user_destinations: Optional[list] = None, licensing_mode: Optional[int] = None,
                    licenses_granted: Optional[list] = None) -> requests.Response:
        json_body = {
            "name": name,
            "password": password,
            "firstName": first_name,
            "lastName": last_name,
            "companyId": company_id,
            "notificationEmails": notification_emails,
            "enabled": enabled,
            "userDestinations": user_destinations,
            "licensingMode": licensing_mode,
            "licensesGranted": licenses_granted
        }
        url = f"{BASE_URI}/{name}"
        return self._session.put(url, json=json_body)
