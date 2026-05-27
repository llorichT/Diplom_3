import allure
import pytest

from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from pages.header import HeaderPage


@allure.feature("Конструктор")
@pytest.mark.constructor
class TestConstructor:
    @allure.title("Переход по клику на «Конструктор»")
    def test_click_constructor_link_opens_constructor(self, driver):
        FeedPage(driver).open_feed()
        HeaderPage(driver).click_constructor()

        assert ConstructorPage(driver).is_constructor_opened()

    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_order_feed_link_opens_feed(self, driver):
        ConstructorPage(driver).open_constructor()
        HeaderPage(driver).click_order_feed()

        assert FeedPage(driver).is_feed_opened()

    @allure.title("При клике на ингредиент открывается модальное окно с деталями")
    def test_ingredient_details_modal_opens(self, driver):
        page = ConstructorPage(driver).open_constructor()
        page.open_first_ingredient_modal()

        assert page.is_ingredient_details_modal_opened()

    @allure.title("Модальное окно с деталями ингредиента закрывается по крестику")
    def test_ingredient_details_modal_closes_by_cross(self, driver):
        page = ConstructorPage(driver).open_constructor()
        page.open_first_ingredient_modal()
        page.close_modal()

        assert page.is_modal_closed()

    @allure.title("При добавлении ингредиента в заказ счётчик ингредиента увеличивается")
    def test_ingredient_counter_increases_after_add_to_order(self, driver):
        page = ConstructorPage(driver).open_constructor()
        before = page.get_first_ingredient_counter()
        page.drag_first_ingredient_to_constructor()
        after = page.get_first_ingredient_counter()

        assert after > before

    @allure.title("Авторизованный пользователь может оформить заказ")
    def test_authorized_user_can_create_order(self, logged_in_driver):
        page = ConstructorPage(logged_in_driver).open_constructor()
        order_number = page.make_order_and_get_number()

        assert order_number.isdigit()