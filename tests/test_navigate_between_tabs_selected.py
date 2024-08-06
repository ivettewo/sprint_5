import time
from conftest import get_element, driver
from locators import Locators


def test_navigation_between_tabs(driver, get_element):
    driver.get(Locators.MAIN_LINK)

    # Нажимаем на кнопку "Начинки"
    get_element(Locators.FILLINGS_BUTTON).click()
    time.sleep(1)
    assert get_element(Locators.FILLINGS_BUTTON_SELECTED), "Кнопка 'Начинки' не выделена"

    # Нажимаем на кнопку "Соусы"
    get_element(Locators.SAUCES_BUTTON).click()
    time.sleep(1)
    assert get_element(Locators.SAUCES_BUTTON_SELECTED), "Кнопка 'Соусы' не выделена"

    # Нажимаем на кнопку "Булки"
    get_element(Locators.BUNS_BUTTON).click()
    time.sleep(1)
    assert get_element(Locators.BUNS_BUTTON_SELECTED), "Кнопка 'Булки' не выделена"

    # Завершаем тест
    driver.quit()
