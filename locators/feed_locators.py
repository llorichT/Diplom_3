from selenium.webdriver.common.by import By


class FeedLocators:
    TOTAL_DONE_COUNTER = (
        By.XPATH,
        "//*[contains(., 'Выполнено за все время') or contains(., 'Выполнено за всё время')]/following::*[contains(@class, 'OrderFeed_number') or contains(@class, 'text_type_digits')][1]",
    )
    TOTAL_TODAY_COUNTER = (
        By.XPATH,
        "//*[contains(., 'Выполнено за сегодня')]/following::*[contains(@class, 'OrderFeed_number') or contains(@class, 'text_type_digits')][1]",
    )
    FIRST_ORDER_CARD = (By.XPATH, "(//a[contains(@href, '/feed/')])[1]")
    ORDER_DETAILS_TITLE = (By.XPATH, "//h2[contains(., 'Детали заказа') or contains(., 'Cостав') or contains(., 'Состав')]")
    IN_PROGRESS_SECTION = (By.XPATH, "//*[contains(., 'В работе')]/following-sibling::*[1]")

    @staticmethod
    def order_number_anywhere(number: str):
        return By.XPATH, f"//*[contains(normalize-space(), '{number}')]"
    
    @staticmethod
    def order_number_in_progress(number: str):
        return (
            By.XPATH,
            f"//*[contains(., 'В работе')]/following-sibling::*[1]//*[contains(normalize-space(), '{number}')]"
        )