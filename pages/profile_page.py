import allure

from pages.base_page import BasePage
from locators.profile_locators import ProfilePageLocators


class ProfilePage(BasePage):
    @allure.step("Перейти в историю заказов")
    def go_to_the_order_history(self):
        if self.driver.name == 'firefox':
            self.js_click(ProfilePageLocators.ORDER_HISTORY)
        else:
            self.click_to_element(ProfilePageLocators.ORDER_HISTORY)

    @allure.step("Выйти из профиля")
    def log_out(self):
        if self.driver.name == 'firefox':
            self.js_click(ProfilePageLocators.LOG_OUT_BUTTON)
        else:
            self.click_to_element(ProfilePageLocators.LOG_OUT_BUTTON)
