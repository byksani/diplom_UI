import pytest
import allure

from pages.feed_page import FeedPage
from data import Urls, Ingredients
from helpers.orders import OrderHelper
from locators.feed_locators import FeedPageLocators


@allure.epic("Тесты страницы ленты заказов")
class TestFeedPage:
    @allure.step("Проверить переход на страницу конструктора")
    def test_go_to_constructor_page(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open()
        feed_page.go_to_the_constructor_page()
        assert feed_page.is_expected_page_loaded(Urls.MAIN_PAGE), \
            "Не удалось перейти на страницу конструктора"

    @allure.story("Проверка счетчиков количества заказов в день и всего")
    @pytest.mark.parametrize(
        "locator",
        [
            FeedPageLocators.ALL_ORDERS_COUNT,
            FeedPageLocators.TODAY_ORDERS
        ]
    )
    def test_orders_count_increase(self, driver, logged_in_user, locator):
        feed_page = FeedPage(driver)
        feed_page.open()

        initial_counter = int(feed_page.get_text_from_element(locator).lstrip('#'))

        OrderHelper.create_order_with_login(
            logged_in_user['email'], logged_in_user['password'], Ingredients.DEFAULT_INGREDIENTS
        )

        new_counter = int(feed_page.get_text_from_element(locator).lstrip('#'))

        assert new_counter == initial_counter + 1, \
            f"Счётчик заказов {locator} не созпадает. Было: {initial_counter}, стало: {new_counter}"

    @allure.story("Проверка отображения последнего созданного заказа в ленте")
    @pytest.mark.parametrize(
        "locator",
        [
            FeedPageLocators.LAST_ORDER_NUMBER,
            FeedPageLocators.ORDER_IN_PROGRESS
        ]
    )
    def test_last_user_order_displayed_correctly(self, driver, logged_in_user, locator):
        feed_page = FeedPage(driver)
        feed_page.open()

        order = OrderHelper.create_order_with_login(
            logged_in_user['email'], logged_in_user['password'], Ingredients.DEFAULT_INGREDIENTS
        )
        created_order_number = str(order["order"]["number"])

        feed_page.wait_for_text_in_element(locator, created_order_number)

        order_text = feed_page.get_text_from_element(locator)

        assert int(order_text.lstrip('#')) == int(created_order_number), \
            f"Номер заказа в элементе ({order_text}) не совпадает с созданным номером ({created_order_number})"

    @allure.step("Проверить что модальное окно с деталями заказа открывается")
    def test_last_order_details_modal_appears(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open()
        feed_page.click_to_the_last_order()
        assert feed_page.is_order_details_modal_visible(), \
            "Модальное окно с деталями заказа не появилось"
