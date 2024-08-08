from conftest import static_data, driver, get_element
from locators import Locators


def test_login_from_forgot_password_page(driver, static_data, get_element):
    driver.get(Locators.FORGOT_PASSWORD_LINK)

    get_element(Locators.LOGIN_BUTTON_ON_ETC_PAGE).click()

    get_element(Locators.EMAIL_INPUT).send_keys(static_data['email'])
    get_element(Locators.PASSWORD_INPUT).send_keys(static_data['password'])

    get_element(Locators.LOGIN_REGISTER_BUTTON_SUBMIT).click()

    get_element(Locators.FILLINGS_BUTTON).is_displayed()
    assert driver.current_url == Locators.MAIN_LINK, f"Текущий URL - {driver.current_url}. \n После регистрации пользователь не попал на главную страницу"
