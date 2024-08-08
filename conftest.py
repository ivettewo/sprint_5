import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def random_word(): # Генератор случайных слов используя буквы нижнего регистра и цифры. В диапазоне от 6 до 8
    length = random.randint(6, 8)
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))

@pytest.fixture # Генератор случайных слов используя буквы нижнего регистра и цифры. В диапазоне от 1 до 5
def random_short_password():
    length = random.randint(1, 5)
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))

@pytest.fixture # Статические данные
def static_data():
    return {
        "email": "evgeniy_s@yandex.com",
        "password": "ASD!3r1"
    }

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture # Поиск элемента в котором встроен WebDriverWait
def get_element(driver):
    def _get_element(locator):
        return WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))
    return _get_element