import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from data import generate_user_data
from helpers.api_client import ApiClient
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="append",
        choices=["chrome", "firefox"],
        help="Браузер для запуска. Можно передать несколько раз. По умолчанию: chrome.",
    )
    parser.addoption("--headless", action="store_true", help="Запустить браузер в headless-режиме")


def pytest_generate_tests(metafunc):
    if "browser_name" in metafunc.fixturenames:
        browsers = metafunc.config.getoption("--browser") or ["chrome"]
        metafunc.parametrize("browser_name", browsers, scope="function")


@pytest.fixture
def driver(browser_name, request):
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-notifications")
        browser = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        browser = webdriver.Firefox(options=options)
        browser.set_window_size(1920, 1080)

    allure.dynamic.label("browser", browser_name)
    yield browser
    browser.quit()


@pytest.fixture
def api_client():
    return ApiClient()


@pytest.fixture
def test_user(api_client):
    user_data = generate_user_data()
    user_response = api_client.create_user(user_data)
    access_token = user_response["accessToken"]
    user_data["access_token"] = access_token

    yield user_data

    api_client.delete_user(access_token)


@pytest.fixture
def logged_in_driver(driver, test_user):
    LoginPage(driver).login(test_user["email"], test_user["password"])
    return driver

@pytest.fixture
def create_order(api_client, test_user):
    def _create_order():
        ingredient_ids = api_client.get_ingredient_ids_for_order()
        return api_client.create_order(
            ingredient_ids,
            test_user["access_token"]
        )
    return _create_order

@pytest.fixture
def created_order_number(create_order):
    order_response = create_order()
    return str(order_response["order"]["number"])