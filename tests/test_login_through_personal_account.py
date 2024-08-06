import time
from conftest import static_data, driver, get_element
from locators import Locators


def test_login_through_personal_account(driver, static_data, get_element):
    driver.get(Locators.MAIN_LINK)

    get_element(Locators.PERSONAL_ACCOUNT_BUTTON).click()

    get_element(Locators.EMAIL_INPUT).send_keys(static_data['email'])
    get_element(Locators.PASSWORD_INPUT).send_keys(static_data['password'])

    get_element(Locators.LOGIN_REGISTER_BUTTON_SUBMIT).click()
    time.sleep(1)
    assert driver.current_url == Locators.MAIN_LINK, f"Текущий URL - {driver.current_url}. \n После регистрации пользователь не попал на главную страницу"

    driver.quit()
