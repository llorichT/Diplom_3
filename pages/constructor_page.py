import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from locators.common_locators import CommonLocators
from locators.constructor_locators import ConstructorLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):
    @allure.step("Открыть конструктор")
    def open_constructor(self):
        self.open("/")
        self.find_visible(ConstructorLocators.FIRST_INGREDIENT_CARD)
        return self

    @allure.step("Открыть карточку первого ингредиента")
    def open_first_ingredient_modal(self):
        self.click(ConstructorLocators.FIRST_INGREDIENT_CARD)
        self.find_visible(ConstructorLocators.INGREDIENT_DETAILS_TITLE)
        return self

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(CommonLocators.MODAL_CLOSE_BUTTON)
        self.wait_until(EC.invisibility_of_element_located(CommonLocators.MODAL))
        return self

    @allure.step("Проверить, что открыт конструктор")
    def is_constructor_opened(self) -> bool:
        return self.current_url().rstrip("/").endswith("stellarburgers.education-services.ru") and self.is_visible(
            ConstructorLocators.FIRST_INGREDIENT_CARD
        )

    @allure.step("Проверить, что модальное окно ингредиента открыто")
    def is_ingredient_details_modal_opened(self) -> bool:
        return self.is_visible(ConstructorLocators.INGREDIENT_DETAILS_TITLE)

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self) -> bool:
        return not self.is_visible(CommonLocators.MODAL, timeout=2)

    @allure.step("Получить счётчик первого ингредиента")
    def get_first_ingredient_counter(self) -> int:
        card = self.find_visible(ConstructorLocators.FIRST_INGREDIENT_CARD)
        try:
            counter = card.find_element(*ConstructorLocators.INGREDIENT_COUNTER_IN_CARD)
            value = counter.text.strip()
            return int(value) if value else 0
        except NoSuchElementException:
            return 0

    def _drag_and_drop(self, source, target):
        self.driver.execute_script(
            """
            function fireDragEvent(type, element, dataTransfer) {
                const event = new DragEvent(type, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                element.dispatchEvent(event);
            }

            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();
            fireDragEvent('pointerdown', source, dataTransfer);
            fireDragEvent('mousedown', source, dataTransfer);
            fireDragEvent('dragstart', source, dataTransfer);
            fireDragEvent('dragenter', target, dataTransfer);
            fireDragEvent('dragover', target, dataTransfer);
            fireDragEvent('drop', target, dataTransfer);
            fireDragEvent('dragend', source, dataTransfer);
            """,
            source,
            target,
        )

    @allure.step("Перетащить первый ингредиент в конструктор")
    def drag_first_ingredient_to_constructor(self):
        source = self.find_visible(ConstructorLocators.FIRST_INGREDIENT_CARD)
        target = self.find_visible(ConstructorLocators.CONSTRUCTOR_DROP_AREA)
        self._drag_and_drop(source, target)
        return self

    @allure.step("Добавить ингредиенты для заказа")
    def add_ingredients_for_order(self):
        drop_area = self.find_visible(ConstructorLocators.CONSTRUCTOR_DROP_AREA)
        bun = self.find_visible(ConstructorLocators.FIRST_BUN_CARD)
        self._drag_and_drop(bun, drop_area)
        ingredient = self.find_visible(ConstructorLocators.FIRST_NON_BUN_CARD)
        self._drag_and_drop(ingredient, drop_area)
        return self

    @allure.step("Оформить заказ и получить его номер")
    def make_order_and_get_number(self) -> str:
        self.add_ingredients_for_order()
        
        order_button = self.find_clickable(ConstructorLocators.ORDER_BUTTON, timeout=30)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_button)
        self.driver.execute_script("arguments[0].click();", order_button)
        self.find_visible(ConstructorLocators.ORDER_MODAL, timeout=60)
        def order_number_is_ready(_):
            number = self.find_visible(ConstructorLocators.ORDER_NUMBER_IN_MODAL, timeout=10).text.strip()
            return number if number and number != "9999" else False
        return self.wait_until(order_number_is_ready, timeout=60)

    @allure.step("Проверить, что окно заказа открыто")
    def is_order_modal_opened(self) -> bool:
        return self.is_visible(ConstructorLocators.ORDER_MODAL, timeout=30)