import allure

from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Авторизоваться пользователем")
    def login(self, email: str, password: str):
        self.open("/login")
        self.find_visible(LoginLocators.EMAIL_INPUT).send_keys(email)
        self.find_visible(LoginLocators.PASSWORD_INPUT).send_keys(password)
        self.click(LoginLocators.LOGIN_SUBMIT_BUTTON)
        self.wait_url_contains("/")
        return self