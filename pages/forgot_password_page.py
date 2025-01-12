import allure

from pages.base_page import BasePage
from data import Urls
from locators.forgot_password_locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):
    @allure.step("Открыть страницу восстановления пароля")
    def open(self):
        self.open_page(Urls.FORGOT_PASSWORD)

    @allure.step("Заполнить поле email: {email}")
    def fill_the_email_field(self, email):
        self.add_text_to_element(ForgotPasswordPageLocators.EMAIL_FIELD, email)

    @allure.step("Нажать на кнопку сохранения")
    def click_to_the_save_button(self):
        self.click_to_element(ForgotPasswordPageLocators.SAVE_BUTTON)

    @allure.step("Нажать на кнопку показа пароля")
    def click_to_the_show_password_button(self):
        if self.driver.name == 'firefox':
            self.js_click(ForgotPasswordPageLocators.SHOW_PASSWORD_BUTTON)
        else:
            self.click_to_element(ForgotPasswordPageLocators.SHOW_PASSWORD_BUTTON)
