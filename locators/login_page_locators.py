from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = By.XPATH, '//input[@name="name"]'
    PASSWORD_FIELD = By.XPATH, '//input[@type="password"]'
    LOGIN_BUTTON = By.XPATH, '//button[text() = "Войти"]'

    FORGOT_PASSWORD_BUTTON = By.XPATH, '//a[text() = "Восстановить пароль"]'
