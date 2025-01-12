from selenium.webdriver.common.by import By


class CommonLocators:
    HEADER_CONSTRUCTOR =By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p[text() = "Конструктор"]'
    HEADER_FEED = By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[2]/a/p[text() = "Лента Заказов"]'
    HEADER_LOGIN_PAGE = By.XPATH, '//*[@id="root"]/div/header/nav/a/p[text() = "Личный Кабинет"]'
