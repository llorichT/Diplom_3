import uuid

BASE_URL = "https://stellarburgers.education-services.ru"
API_URL = f"{BASE_URL}/api"
DEFAULT_TIMEOUT = 15
TEST_EMAIL_DOMAIN = "yandex.ru"
TEST_PASSWORD = "Password123"
TEST_NAME = "Anastasia Test"


def generate_user_data() -> dict:
    return {
        "email": f"test_user_{uuid.uuid4().hex}@{TEST_EMAIL_DOMAIN}",
        "password": TEST_PASSWORD,
        "name": TEST_NAME,
    }