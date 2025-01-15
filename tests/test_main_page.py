import allure

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data import Urls


@allure.epic("Тесты главной страницы")
class TestMainPage:
    @allure.step("Проверить переход на страницу профиля для авторизованного пользователя")
    def test_navigate_to_the_profile_page(self, driver, logged_in_user):
        main_page = MainPage(driver)
        main_page.click_to_the_login_page_button()
        assert main_page.is_expected_page_loaded(Urls.PROFILE_PAGE), \
            f"Не удалось перейти на страницу профиля. Текущий URL: {driver.current_url}"

    @allure.step("Проверить переход на страницу ленты заказов")
    def test_go_to_feed_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_to_the_feed_page_button()
        assert main_page.is_expected_page_loaded(Urls.FEED), \
            f"Не удалось перейти на страницу ленты заказов. Текущий URL: {driver.current_url}"

    @allure.step("Проверить что модульное окно с детализацией ингридиента открывается")
    def test_ingredient_modal_appears(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_to_the_ingredient()
        assert main_page.is_ingredient_modal_visible(), \
            f"Модальное окно с деталями ингредиента не появилось"

    @allure.step("Проверить закрытие модального окна с детализацией ингридиента")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_to_the_ingredient()
        main_page.close_ingredient_modal()
        assert main_page.is_ingredient_modal_invisible(), \
            f"Модальное окно не закрылось"


    @allure.step("Проверить увеличение счётчика ингредиента после добавления в корзину")
    def test_ingredient_counter_increases_after_drag(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        initial_counter = int(main_page.get_text_from_element(MainPageLocators.COUNTER))

        main_page.drag_ingredient_to_cart(MainPageLocators.INGREDIENT, MainPageLocators.CARD_AREA)

        new_counter = int(main_page.get_text_from_element(MainPageLocators.COUNTER))
        assert new_counter == initial_counter + 2, \
            f"Счётчик ингредиентов не увеличился. Было: {initial_counter}, стало: {new_counter}"

    @allure.step("Проверить создание заказа авторизованным пользователем")
    def test_logged_in_user_can_create_an_order(self, driver, logged_in_user):
        main_page = MainPage(driver)
        main_page.drag_ingredient_to_cart(MainPageLocators.INGREDIENT, MainPageLocators.CARD_AREA)

        main_page.click_to_the_create_order_button()
        assert main_page.is_order_modal_visible(), \
            f"Модальное окно для созданного заказа не появилось"
