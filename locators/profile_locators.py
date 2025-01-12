from selenium.webdriver.common.by import By


class ProfilePageLocators:
    ORDER_HISTORY = By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[2]/a[text() = "История заказов"]'
    LOG_OUT_BUTTON = By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button[text() = "Выход"]'
