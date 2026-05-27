from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import DEFAULT_TIMEOUT


def wait_visible(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))


def wait_clickable(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


def wait_url_contains(driver, part, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.url_contains(part))


def wait_text_present(driver, locator, text, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.text_to_be_present_in_element(locator, text))