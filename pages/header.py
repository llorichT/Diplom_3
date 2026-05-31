import allure

from locators.common_locators import CommonLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    @allure.step("Кликнуть по ссылке «Конструктор»")
    def click_constructor(self):
        self.click(CommonLocators.CONSTRUCTOR_LINK)
        return self

    @allure.step("Кликнуть по ссылке «Лента заказов»")
    def click_order_feed(self):
        self.click(CommonLocators.ORDER_FEED_LINK)
        return self