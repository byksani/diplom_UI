from selenium.webdriver.common.by import By


class MainPageLocators:
    INGREDIENT = (
        By.XPATH, '(//ul[contains(@class, "BurgerIngredients_ingredients__list")])[1]/a[1]')
    INGREDIENT_MODAL_WINDOW = (
        By.XPATH, '(//div[contains(@class, "Modal_modal__contentBox")])[1]')
    INGREDIENT_CLOSE_WINDOW = (
        By.XPATH, '(//button[contains(@class, "Modal_modal__close_modified")])[1]')

    CARD_AREA = (
        By.XPATH, '//*[@id="root"]/div/main/section[2]/ul')
    COUNTER = (
        By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/div[1]/p')

    ORDER_BUTTON = (
        By.XPATH, '//button[text() = "Оформить заказ"]')
    ORDER_MODAL_WINDOW = (
        By.XPATH, '//*[@id="root"]/div/section/div[1]')
