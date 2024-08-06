import time
from conftest import static_data, driver, get_element
from locators import Locators


def test_personal_account_redirect_if_authorized(driver, static_data, get_element):
    driver.get(Locators.LOGIN_LINK)

    get_element(Locators.EMAIL_INPUT).send_keys(static_data['email'])
    get_element(Locators.PASSWORD_INPUT).send_keys(static_data['password'])

    get_element(Locators.LOGIN_REGISTER_BUTTON_SUBMIT).click()
    time.sleep(2)

    assert driver.current_url == Locators.MAIN_LINK, f"Текущий URL - {driver.current_url}. \n После регистрации пользователь не попал на главную страницу"

    get_element(Locators.PERSONAL_ACCOUNT_BUTTON).click()
    time.sleep(2)

    assert driver.current_url == Locators.PROFILE_LINK, f"Текущий URL - {driver.current_url}. \n Страница Profile не открыта"

    driver.quit()