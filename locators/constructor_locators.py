from selenium.webdriver.common.by import By


class ConstructorLocators:
    FIRST_INGREDIENT_CARD = (
        By.XPATH,
        "(//p[contains(@class, 'BurgerIngredient_ingredient__text')]/ancestor::a)[1]",
    )
    FIRST_BUN_CARD = (By.XPATH, "(//p[contains(text(), 'булка')]/ancestor::a)[1]")
    FIRST_NON_BUN_CARD = (
        By.XPATH,
        "(//p[not(contains(text(), 'булка')) and contains(@class, 'BurgerIngredient_ingredient__text')]/ancestor::a)[1]",
    )
    INGREDIENT_COUNTER_IN_CARD = (By.XPATH, ".//*[contains(@class, 'counter_counter__num')]")
    INGREDIENT_DETAILS_TITLE = (By.XPATH, "//h2[contains(., 'Детали ингредиента')]")
    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ') and not(@disabled)]")
    ORDER_NUMBER_IN_MODAL = (
        By.XPATH,
        "//h2[contains(@class, 'text_type_digits-large')]",
    )
    ORDER_MODAL_TITLE = (
        By.XPATH,
        "//*[contains(., 'идентификатор заказа') or contains(., 'Ваш заказ начали готовить')]",
    )
    ORDER_MODAL = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal_opened')]"
    )