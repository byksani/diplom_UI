import allure

from pages.login_page import LoginPage
from data import Urls


@allure.epic("Тесты страницы авторизации")
class TestLoginPage:
    @allure.step("Проверить переход на страницу восстановления пароля")
    def test_navigate_to_the_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_to_the_forgot_password_page_button()
        assert login_page.is_expected_page_loaded(Urls.FORGOT_PASSWORD), \
            f"Не удалось перейти на страницу восстановления пароля. Текущий URL: {driver.current_url}"
