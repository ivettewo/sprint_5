from conftest import static_data, get_element, driver
from locators import Locators


def test_login_success(static_data, get_element, driver):
    driver.get(Locators.MAIN_LINK)

    get_element(Locators.ENTER_LOGIN_PAGE_BUTTON).click()

    get_element(Locators.EMAIL_INPUT).send_keys(static_data['email'])
    get_element(Locators.PASSWORD_INPUT).send_keys(static_data['password'])

    # Нажимаем кнопку "Войти"
    get_element(Locators.LOGIN_REGISTER_BUTTON_SUBMIT).click()

    get_element(Locators.FILLINGS_BUTTON).is_displayed()
    assert driver.current_url == Locators.MAIN_LINK, f"Текущий URL - {driver.current_url}. \n После регистрации пользователь не попал на главную страницу"
