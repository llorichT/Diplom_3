import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from data import BASE_URL, DEFAULT_TIMEOUT



class BasePage:
    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.timeout = timeout

    @allure.step("Открыть страницу: {path}")
    def open(self, path="/"):
        self.driver.get(f"{BASE_URL}{path}")
        return self

    @allure.step("Найти видимый элемент")
    def find_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Найти кликабельный элемент")
    def find_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Кликнуть по элементу")
    def click(self, locator, timeout=DEFAULT_TIMEOUT):
        self.find_clickable(locator, timeout).click()
        return self

    @allure.step("Проверить видимость элемента")
    def is_visible(self, locator, timeout=DEFAULT_TIMEOUT) -> bool:
        try:
            self.find_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    @allure.step("Дождаться, что элемент станет невидимым")
    def wait_invisible(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Дождаться, что URL содержит текст: {text}")
    def wait_url_contains(self, text, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(text))
        
    @allure.step("Дождаться выполнения условия")
    def wait_until(self, condition, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(condition)

    @allure.step("Получить текущий URL")
    def current_url(self) -> str:
        return self.driver.current_url

    @allure.step("Дождаться изменения URL")
    def wait_url_changes(self, old_url, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_changes(old_url)
        )

    @allure.step("Проверить, что текущий URL содержит текст: {text}")
    def is_current_url_contains(self, text: str) -> bool:
        return text in self.current_url()

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return self

    @allure.step("Перетащить элемент")
    def drag_and_drop(self, source, target):
        ActionChains(self.driver).drag_and_drop(source, target).perform()
        return self