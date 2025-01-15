from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    EMAIL_FIELD = By.XPATH, '//input[@name="name"]'
    SAVE_BUTTON = By.XPATH, '//button[text() = "Восстановить"]'

    PASSWORD_FIELD = By.XPATH, '//input[@name="Введите новый пароль"]'
    SHOW_PASSWORD_BUTTON = By.XPATH, '//div[contains(@class, "input__icon")]'

