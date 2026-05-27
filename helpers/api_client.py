import requests

from data import API_URL


class ApiClient:
    def __init__(self):
        self.session = requests.Session()

    def create_user(self, user_data: dict) -> dict:
        response = self.session.post(f"{API_URL}/auth/register", json=user_data, timeout=30)
        response.raise_for_status()
        return response.json()

    def login(self, email: str, password: str) -> dict:
        response = self.session.post(
            f"{API_URL}/auth/login",
            json={"email": email, "password": password},
            timeout=15,
        )
        response.raise_for_status()
        return response.json()

    def delete_user(self, access_token: str) -> None:
        response = self.session.delete(
            f"{API_URL}/auth/user",
            headers={"Authorization": access_token},
            timeout=15,
        )
        response.raise_for_status()

    def get_ingredients(self) -> list[dict]:
        response = self.session.get(f"{API_URL}/ingredients", timeout=15)
        response.raise_for_status()
        return response.json()["data"]

    def create_order(self, ingredient_ids: list[str], access_token: str | None = None) -> dict:
        headers = {"Authorization": access_token} if access_token else {}
        response = self.session.post(
            f"{API_URL}/orders",
            json={"ingredients": ingredient_ids},
            headers=headers,
            timeout=15,
        )
        response.raise_for_status()
        return response.json()