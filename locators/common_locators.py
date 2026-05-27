from selenium.webdriver.common.by import By


class CommonLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//a[contains(., 'Конструктор')]")
    ORDER_FEED_LINK = (
        By.XPATH,
        "//a[contains(@href, '/feed') or .//*[contains(text(), 'Лента заказов')] or contains(text(), 'Лента заказов')]",
    )
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//button")