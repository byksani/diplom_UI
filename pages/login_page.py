import allure

from pages.base_page import BasePage
from data import Urls
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    @allure.step("Открыть страницу входа")
    def open(self):
        self.open_page(Urls.LOGIN_PAGE)

    @allure.step("Перейти на страницу восстановления пароля")
    def click_to_the_forgot_password_page_button(self):
        self.click_to_element(LoginPageLocators.FORGOT_PASSWORD_BUTTON)
