import allure

from locators.feed_locators import FeedLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step("Открыть ленту заказов")
    def open_feed(self):
        self.open("/feed")
        self.find_visible(FeedLocators.TOTAL_DONE_COUNTER)
        return self

    @allure.step("Проверить, что открыта лента заказов")
    def is_feed_opened(self) -> bool:
        return "/feed" in self.current_url() and self.is_visible(FeedLocators.TOTAL_DONE_COUNTER)

    @allure.step("Открыть детали первого заказа")
    def open_first_order_details(self):
        old_url = self.current_url()
        order = self.find_visible(FeedLocators.FIRST_ORDER_CARD)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order)
        self.driver.execute_script("arguments[0].click();", order)
        self.wait_url_changes(old_url)

    @allure.step("Получить счётчик «Выполнено за всё время»")
    def get_total_done(self) -> int:
        return int(self.find_visible(FeedLocators.TOTAL_DONE_COUNTER).text.replace(" ", ""))

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def get_total_today(self) -> int:
        return int(self.find_visible(FeedLocators.TOTAL_TODAY_COUNTER).text.replace(" ", ""))

    @allure.step("Дождаться увеличения счётчика «Выполнено за всё время»")
    def wait_total_done_more_than(self, old_value: int):
        return self.wait_until(lambda _: self.get_total_done() > old_value, timeout=60)

    @allure.step("Дождаться увеличения счётчика «Выполнено за сегодня»")
    def wait_total_today_more_than(self, old_value: int):
        return self.wait_until(lambda _: self.get_total_today() > old_value, timeout=60)

    @allure.step("Проверить, что номер заказа отображается")
    def is_order_number_visible(self, number: str) -> bool:
        return self.is_visible(FeedLocators.order_number_anywhere(number), timeout=30)

    @allure.step("Дождаться появления номера заказа")
    def wait_order_number_appears(self, number: str):
        self.wait_until(lambda _: self.is_order_number_visible(number), timeout=60)
        return self

    @allure.step("Проверить, что заказ появился в разделе «В работе»")
    def is_order_in_progress(self, number: str) -> bool:
        normalized_number = number.lstrip("0")
        return self.is_visible(
            FeedLocators.order_number_in_progress(normalized_number),
            timeout=60
        )