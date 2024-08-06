import pytest
import random
import string
from selenium import webdriver

@pytest.fixture
def random_word():
    length = random.randint(6, 8)
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))

@pytest.fixture
def random_short_password():
    length = random.randint(1, 5)
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))

@pytest.fixture
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

@pytest.fixture
def get_element(driver):
    def _get_element(locator):
        return driver.find_element(*locator)
    return _get_element
