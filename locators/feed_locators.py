from selenium.webdriver.common.by import By


class FeedPageLocators:
    LAST_ORDER = By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li[1]'
    LAST_ORDER_NUMBER = By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li[1]/a/div[1]/p[1]'
    ORDER_MODAL_WINDOW = By.XPATH, '//*[@id="root"]/div/section[2]/div[1]'
    ORDER_IN_PROGRESS = By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/ul[2]/li'

    ALL_ORDERS_COUNT = By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[2]/p[2]'
    TODAY_ORDERS = By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[3]/p[2]'
