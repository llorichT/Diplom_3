import allure
import pytest

from pages.feed_page import FeedPage


@allure.feature("Лента заказов")
@pytest.mark.feed
class TestOrderFeed:
    @allure.title("При клике на заказ открывается модальное окно с деталями")
    def test_order_details_modal_opens(self, driver):
        page = FeedPage(driver).open_feed()
        page.open_first_order_details()

        assert page.is_order_details_opened()

    @allure.title("После создания заказа его номер появляется в ленте заказов")
    def test_created_order_number_appears_in_feed(self, logged_in_driver, created_order_number):
        feed = FeedPage(logged_in_driver).open_feed()
        feed.wait_order_number_appears(created_order_number)

        assert feed.is_order_number_visible(created_order_number)

    @allure.title("После создания заказа счётчик «Выполнено за всё время» увеличивается")
    def test_total_done_counter_increases_after_new_order(self, logged_in_driver, create_order):
        feed = FeedPage(logged_in_driver).open_feed()
        old_total = feed.get_total_done()
        create_order()
        feed.open_feed()
        feed.wait_total_done_more_than(old_total)

        assert feed.get_total_done() > old_total

    @allure.title("После создания заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_total_today_counter_increases_after_new_order(self, logged_in_driver, create_order):
        feed = FeedPage(logged_in_driver).open_feed()
        old_total_today = feed.get_total_today()
        create_order()
        feed.open_feed()
        feed.wait_total_today_more_than(old_total_today)

        assert feed.get_total_today() > old_total_today

    @allure.title("После создания заказа его номер появляется в разделе «В работе»")
    def test_created_order_appears_in_progress(self, logged_in_driver, created_order_number):
        feed = FeedPage(logged_in_driver).open_feed()

        assert feed.is_order_in_progress(created_order_number)