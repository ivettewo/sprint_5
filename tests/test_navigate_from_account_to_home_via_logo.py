from conftest import static_data, driver, get_element
from locators import Locators


def test_navigate_from_account_to_home_via_logo(driver, static_data, get_element):
    user_data = static_data

    # Авторизация
    driver.get(Locators.LOGIN_LINK)

    get_element(Locators.EMAIL_VALUE).send_keys(user_data['email'])
    get_element(Locators.PASSWORD_INPUT).send_keys(user_data['password'])

    get_element(Locators.LOGIN_REGISTER_BUTTON_SUBMIT).click()

    # Переход на страницу профиля
    get_element(Locators.PERSONAL_ACCOUNT_BUTTON).click()

    get_element(Locators.LOGO_BUTTON).click()

    get_element(Locators.FILLINGS_BUTTON).is_displayed()
    assert driver.current_url == Locators.MAIN_LINK, f"Ожидался URL {Locators.MAIN_LINK}, но получен {driver.current_url}"
