from conftest import static_data, driver, get_element
from locators import Locators


def test_logout_from_account(driver, static_data, get_element):
    user_data = static_data

    # Авторизация
    driver.get(Locators.LOGIN_LINK)

    get_element(Locators.EMAIL_VALUE).send_keys(user_data['email'])
    get_element(Locators.PASSWORD_INPUT).send_keys(user_data['password'])

    get_element(Locators.LOGIN_REGISTER_BUTTON_SUBMIT).click()

    get_element(Locators.PERSONAL_ACCOUNT_BUTTON).click()

    get_element(Locators.LOGOUT_BUTTON).click()
    get_element(Locators.AUTH_LOGIN_ELEMENTS).is_displayed()

    assert driver.current_url == Locators.LOGIN_LINK, f"Ожидался URL {Locators.LOGIN_LINK}, но получен {driver.current_url}"
