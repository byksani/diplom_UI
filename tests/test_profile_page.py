import allure

from data import Urls
from pages.profile_page import ProfilePage
from locators.common_locators import CommonLocators


@allure.epic("Тесты страницы профиля")
class TestProfilePage:
    @allure.step("Проверить переход в историю заказов для авторизованного пользователя")
    def test_go_to_the_order_history(self, driver, logged_in_user):
        profile_page = ProfilePage(driver)
        profile_page.click_to_element(CommonLocators.HEADER_LOGIN_PAGE)

        profile_page.go_to_the_order_history()
        assert profile_page.is_expected_page_loaded(Urls.ORDER_HISTORY), \
            f"Не удалось перейти в историю заказов. Текущий URL: {driver.current_url}"

    @allure.step("Проверить выход из аккаунта авторизованного пользователя")
    def test_log_out_from_the_account(self, driver, logged_in_user):
        profile_page = ProfilePage(driver)
        profile_page.click_to_element(CommonLocators.HEADER_LOGIN_PAGE)

        profile_page.log_out()
        assert profile_page.is_expected_page_loaded(Urls.LOGIN_PAGE), \
            f"Не удалось выйти из аккаунта. Текущий URL: {driver.current_url}"
