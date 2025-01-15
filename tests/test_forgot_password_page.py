import allure

from data import Urls
from pages.forgot_password_page import ForgotPasswordPage
from locators.forgot_password_locators import ForgotPasswordPageLocators


@allure.epic("Тесты страницы восстановления пароля")
class TestForgotPasswordPage:
    @allure.step("Проверить заполнение email и переход на страницу сброса пароля")
    def test_fill_email_and_go_to_the_password_page(self, driver, random_user_data):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open()

        forgot_password_page.fill_the_email_field(random_user_data['email'])
        forgot_password_page.click_to_the_save_button()

        assert forgot_password_page.is_expected_page_loaded(Urls.RESET_PASSWORD), \
            f"Не удалось перейти на страницу сброса пароля. Текущий URL: {driver.current_url}"

    @allure.step("Проверить активацию поля пароля при клике на кнопку 'Показать пароль'")
    def test_password_field_activation_on_show_password_click(self, driver, random_user_data):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open()

        forgot_password_page.fill_the_email_field(random_user_data['email'])
        forgot_password_page.click_to_the_save_button()

        forgot_password_page.click_to_the_show_password_button()
        field_type = forgot_password_page.get_field_attribute(ForgotPasswordPageLocators.PASSWORD_FIELD, 'type')

        assert field_type == 'text', \
            f"Поле пароля не активировано. Ожидалось: 'text', но получено: '{field_type}'"
