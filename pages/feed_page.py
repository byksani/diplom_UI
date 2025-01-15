import allure

from pages.base_page import BasePage
from data import Urls
from locators.common_locators import CommonLocators
from locators.feed_locators import FeedPageLocators


class FeedPage(BasePage):
    @allure.step("Открыть страницу ленты заказов")
    def open(self):
        self.open_page(Urls.FEED)

    @allure.step("Перейти на страницу конструктора")
    def go_to_the_constructor_page(self):
        if self.driver.name == 'firefox':
            self.js_click(CommonLocators.HEADER_CONSTRUCTOR)
        else:
            self.click_to_element(CommonLocators.HEADER_CONSTRUCTOR)

    @allure.step("Кликнуть по последнему заказу в ленте")
    def click_to_the_last_order(self):
        self.click_to_element(FeedPageLocators.LAST_ORDER)

    @allure.step("Проверить, что модальное окно с деталями заказа отображается")
    def is_order_details_modal_visible(self):
        return self.is_modal_window_visible(FeedPageLocators.ORDER_MODAL_WINDOW)
