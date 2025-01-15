import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу: {url}")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент с ожиданием: {locator}")
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                locator))
        return self.driver.find_element(*locator)

    @allure.step("Кликнуть по элементу: {locator}")
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step("Кликнуть по элементу через JavaScript: {locator}")
    def js_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Добавить текст '{text}' в элемент: {locator}")
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Получить текст из элемента: {locator}")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("Проверить текущую страницу: {expected_url}")
    def is_expected_page_loaded(self, expected_url):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.url_to_be(expected_url)
            )
            return True
        except Exception:
            return False

    @allure.step("Проверить, что атрибут у элемента {locator}")
    def get_field_attribute(self, locator, field):
        return self.driver.find_element(*locator).get_attribute(field)

    @allure.step("Проверить, что модальное окно отображается")
    def is_modal_window_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_window_invisible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.invisibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    @allure.step("Ожидаю появления текста '{expected_text}' в элементе: {locator}")
    def wait_for_text_in_element(self, locator, expected_text):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.text_to_be_present_in_element(locator, expected_text),
            message=f"Текст '{expected_text}' не появился в элементе {locator}"
        )
