from selenium.webdriver.common.by import By


class MainPageLocators:
    INGREDIENT = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]'
    INGREDIENT_MODAL_WINDOW = By.XPATH, '//*[@id="root"]/div/section[1]/div[1]/div'
    INGREDIENT_CLOSE_WINDOW = By.XPATH, '//*[@id="root"]/div/section[1]/div[1]/button'

    CARD_AREA = By.XPATH, '//*[@id="root"]/div/main/section[2]/ul'
    COUNTER = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/div[1]/p'

    ORDER_BUTTON = By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button[text() = "Оформить заказ"]'
    ORDER_MODAL_WINDOW = By.XPATH, '//*[@id="root"]/div/section/div[1]'
