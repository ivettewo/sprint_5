from conftest import driver, get_element
from locators import Locators


def test_personal_account_redirect_not_logged_in(driver, get_element):
    driver.get(Locators.MAIN_LINK)
    get_element(Locators.PERSONAL_ACCOUNT_BUTTON).click()
    assert driver.current_url == Locators.LOGIN_LINK, f"Текущий URL - {driver.current_url}. \n Ожидался переход на страницу входа"

    driver.quit()
