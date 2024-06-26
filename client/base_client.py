import os
from base64 import b64encode

import requests


class BaseClient:
    def __init__(self):
        self._session: requests.Session = requests.Session()
        self._session.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"{self._basic_auth(os.environ.get('USERNAME'), os.environ.get('PASSWORD'))}",
        }

    @staticmethod
    def _basic_auth(username, password):
        token = b64encode(f"{username}:{password}".encode("utf-8")).decode("ascii")
        return f"Basic {token}"
