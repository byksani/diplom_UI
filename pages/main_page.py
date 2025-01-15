import allure

from pages.base_page import BasePage
from data import Urls
from locators.common_locators import CommonLocators
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open(self):
        self.open_page(Urls.MAIN_PAGE)

    @allure.step("Перейти на страницу входа в аккаунт")
    def click_to_the_login_page_button(self):
        self.click_to_element(CommonLocators.HEADER_LOGIN_PAGE)

    @allure.step("Перейти на страницу ленты заказов")
    def click_to_the_feed_page_button(self):
        self.click_to_element(CommonLocators.HEADER_FEED)

    @allure.step("Кликнуть на кнопку создания заказа")
    def click_to_the_create_order_button(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON)

    @allure.step("Кликнуть на ингредиент")
    def click_to_the_ingredient(self):
        self.click_to_element(MainPageLocators.INGREDIENT)

    @allure.step("Проверить, что модальное окно ингредиента отображается")
    def is_ingredient_modal_visible(self):
        return self.is_modal_window_visible(MainPageLocators.INGREDIENT_MODAL_WINDOW)

    @allure.step("Проверить, что модальное окно заказа отображается")
    def is_order_modal_visible(self):
        return self.is_modal_window_visible(MainPageLocators.ORDER_MODAL_WINDOW)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click_to_element(MainPageLocators.INGREDIENT_CLOSE_WINDOW)

    @allure.step("Проверить, что модальное окно ингредиента закрыто")
    def is_ingredient_modal_invisible(self):
        return self.is_modal_window_invisible(MainPageLocators.INGREDIENT_MODAL_WINDOW)

    @allure.step("Перетащить ингредиент в корзину")
    def drag_ingredient_to_cart(self, ingredient_locator, cart_locator):
        ingredient = self.find_element_with_wait(ingredient_locator)
        cart_area = self.find_element_with_wait(cart_locator)

        if self.driver.name == 'firefox':
            self.driver.execute_script("""
                        const dataTransfer = new DataTransfer();
                        arguments[0].dispatchEvent(new DragEvent('dragstart', { bubbles: true, cancelable: true, dataTransfer }));
                        arguments[1].dispatchEvent(new DragEvent('dragover', { bubbles: true, cancelable: true, dataTransfer }));
                        arguments[1].dispatchEvent(new DragEvent('drop', { bubbles: true, cancelable: true, dataTransfer }));
                        arguments[0].dispatchEvent(new DragEvent('dragend', { bubbles: true, cancelable: true, dataTransfer }));
                    """, ingredient, cart_area)

        else:
            action = ActionChains(self.driver)
            action.drag_and_drop(ingredient, cart_area).perform()
