from selenium.webdriver.common.by import By


class ProfilePageLocators:
    ORDER_HISTORY = By.XPATH, '//a[text() = "История заказов"]'
    LOG_OUT_BUTTON = By.XPATH, '//button[text() = "Выход"]'
