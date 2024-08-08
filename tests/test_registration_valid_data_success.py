import time
from conftest import random_word, get_element, driver
from locators import Locators


def test_registration_valid_data_success(random_word, get_element, driver):
    driver.get(Locators.MAIN_LINK)

    name = random_word
    email = random_word + "@ya.ru"
    password = random_word

    get_element(Locators.PERSONAL_ACCOUNT_BUTTON).click()

    auth_login_elements = driver.find_elements(*Locators.AUTH_LOGIN_ELEMENTS)
    assert auth_login_elements, "Элемент страницы Вход не найден"

    get_element(Locators.REGISTER_BUTTON).click()

    get_element(Locators.NAME_INPUT).send_keys(name)
    get_element(Locators.EMAIL_INPUT).send_keys(email)
    get_element(Locators.PASSWORD_INPUT).send_keys(password)

    get_element(Locators.LOGIN_REGISTER_BUTTON_SUBMIT).click()

    # Авторизация (без while иногда не срабатывает)
    while True:
        get_element(Locators.EMAIL_INPUT).clear()
        get_element(Locators.PASSWORD_INPUT).clear()

        get_element(Locators.EMAIL_INPUT).send_keys(email)
        get_element(Locators.PASSWORD_INPUT).send_keys(password)

        # Проверяем правильность введенных данных
        email_value = get_element(Locators.EMAIL_INPUT).get_attribute("value")
        password_value = get_element(Locators.PASSWORD_INPUT).get_attribute("value")

        if email_value == email and password_value == password:
            break
        else:
            print("Неверные данные, повторяем ввод")

    get_element(Locators.LOGIN_REGISTER_BUTTON_SUBMIT).click()

    get_element(Locators.FILLINGS_BUTTON).is_displayed()
    get_element(Locators.PERSONAL_ACCOUNT_BUTTON).click()

    name_value = get_element(Locators.NAME_VALUE).get_attribute("value")
    assert name_value == name, f"Ожидаем '{name}' в поле 'Имя', но получено '{name_value}'"

    email_value = get_element(Locators.EMAIL_VALUE).get_attribute("value")
    assert email_value == email, f"Ожидаем '{email}' в поле 'Email', но получено '{email_value}'"