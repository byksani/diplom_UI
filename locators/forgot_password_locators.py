from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    EMAIL_FIELD = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset/div/div/input'
    SAVE_BUTTON = By.XPATH, '//*[@id="root"]/div/main/div/form/button[text() = "Восстановить"]'

    PASSWORD_FIELD = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
    SHOW_PASSWORD_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/div')
