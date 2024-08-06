import time
from conftest import random_word, random_short_password, driver, get_element
from locators import Locators


def test_registration_short_password_error(driver, random_word, random_short_password, get_element):
    driver.get(Locators.MAIN_LINK)

    get_element(Locators.PERSONAL_ACCOUNT_BUTTON).click()
    time.sleep(1)

    get_element(Locators.REGISTER_BUTTON).click()

    get_element(Locators.NAME_INPUT).send_keys(random_word)
    get_element(Locators.EMAIL_INPUT).send_keys(random_word + "@ya.ru")
    get_element(Locators.PASSWORD_INPUT).send_keys(random_short_password)

    get_element(Locators.LOGIN_REGISTER_BUTTON_SUBMIT).click()
    time.sleep(1)

    # Проверяем, что у инпута есть класс input_status_error - То есть красная рамка
    password_input_container = get_element(Locators.PASSWORD_INPUT_ERROR_BORDER)
    assert password_input_container is not None, "Класс 'input_status_error' не найден - Рамка не красная"

    driver.quit()
