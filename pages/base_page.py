import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import BASE_URL, DEFAULT_TIMEOUT
from helpers.waits import wait_clickable, wait_visible


class BasePage:
    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.timeout = timeout

    @allure.step("Открыть страницу: {path}")
    def open(self, path="/"):
        self.driver.get(f"{BASE_URL}{path}")
        return self

    def find_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        return wait_visible(self.driver, locator, timeout)

    def find_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        return wait_clickable(self.driver, locator, timeout)

    def click(self, locator, timeout=DEFAULT_TIMEOUT):
        self.find_clickable(locator, timeout).click()
        return self

    def is_visible(self, locator, timeout=DEFAULT_TIMEOUT) -> bool:
        try:
            self.find_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    def wait_url_contains(self, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(text))
        

    def wait_until(self, condition, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(condition)

    def current_url(self) -> str:
        return self.driver.current_url

    def wait_url_changes(self, old_url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_changes(old_url)
        )