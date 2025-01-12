from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
    PASSWORD_FIELD = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'
    LOGIN_BUTTON = By.XPATH, '//*[@id="root"]/div/main/div/form/button[text() = "Войти"]'

    FORGOT_PASSWORD_BUTTON = By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a[text() = "Восстановить пароль"]'
