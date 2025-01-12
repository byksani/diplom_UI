import pytest
import random
import string
import requests

from selenium import webdriver
from data import Requests, Urls
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(params=["firefox", "chrome"])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    yield driver

    driver.quit()

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

@pytest.fixture
def random_user_data():
    name = generate_random_string(6)
    email = f'{generate_random_string(8)}@test.com'
    password = generate_random_string(10)

    return {
        'name': name,
        'email': email,
        'password': password
    }

@pytest.fixture
def created_user(random_user_data):
    response = requests.post(Requests.REGISTER, json=random_user_data)
    response_context = response.json()

    yield random_user_data

    requests.delete(Requests.USER, headers={'Authorization': response_context['accessToken']})

@pytest.fixture
def logged_in_user(driver, created_user):
    driver.get(Urls.LOGIN_PAGE)

    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(created_user['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(created_user['password'])

    login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
    driver.execute_script("arguments[0].click();", login_button)

    WebDriverWait(driver, 10).until(
        expected_conditions.url_to_be(Urls.MAIN_PAGE),
        message="URL не изменился на главную страницу после входа"
    )

    assert driver.current_url == Urls.MAIN_PAGE, "Не удалось выполнить вход"
    return created_user
