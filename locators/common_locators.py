from selenium.webdriver.common.by import By


class CommonLocators:
    HEADER_CONSTRUCTOR = By.XPATH, '//p[text()="Конструктор"]'
    HEADER_FEED = By.XPATH, '//p[text() = "Лента Заказов"]'
    HEADER_LOGIN_PAGE = By.XPATH, '//p[text() = "Личный Кабинет"]'
