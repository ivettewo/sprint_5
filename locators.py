from selenium.webdriver.common.by import By

# Сначала описание кнопки
# затем идет слеш "/" который обозначает на какой странице кнопка
class Locators:
    AUTH_LOGIN_ELEMENTS = (By.CSS_SELECTOR, "div.Auth_login__3hAey")  # Элемент страницы авторизации для проверки наличия /login
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка перехода в конструктор /
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле ввода email /login /register /forgot-password
    EMAIL_VALUE = (By.XPATH, "//input[@name='name']")  # Поле email для проверки значения /account/profile
    LOGIN_BUTTON_ON_ETC_PAGE = (By.CSS_SELECTOR, "a.Auth_link__1fOlj[href='/login']")  # Кнопка "Войти" в самом низу страницы регистрации и восстановления пароля /register /forgot-password
    LOGIN_REGISTER_BUTTON_SUBMIT = (By.CSS_SELECTOR, "button.button_button_size_medium__3zxIa")  # Кнопка подтверждения входа "Войти" и регистрации "Зарегистрироваться"
    ENTER_LOGIN_PAGE_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в Аккаунт" на главной странице /
    LOGO_BUTTON = (By.CSS_SELECTOR, "div.AppHeader_header__logo__2D0X2 a[href='/']")  # Кнопка логотипа для перехода на главную страницу
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода из аккаунта /account/profile
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='name']")  # Поле ввода имени /register
    NAME_VALUE = (By.XPATH, "//input[@name='Name']")  # Поле имени для проверки значения /account/profile
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password'][name='Пароль']")  # Поле ввода пароля /login /register /forgot-password
    PASSWORD_INPUT_ERROR_BORDER = (By.CSS_SELECTOR, "div.input_status_error")  # Красная рамка поле ввода пароля с ошибкой /register
    PERSONAL_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a[href='/account']")  # Кнопка перехода в личный кабинет
    REGISTER_BUTTON = (By.CSS_SELECTOR, "a.Auth_link__1fOlj")  # Кнопка перехода на страницу регистрации /login

    # Ссылки
    MAIN_LINK = "https://stellarburgers.nomoreparties.site/"  # Главная страница /main
    LOGIN_LINK = "https://stellarburgers.nomoreparties.site/login"  # Страница Логина /login
    REGISTER_LINK = "https://stellarburgers.nomoreparties.site/register"  # Страница регистрации /register
    FORGOT_PASSWORD_LINK = "https://stellarburgers.nomoreparties.site/forgot-password"  # Страница восстановления пароля /forgot-password
    PROFILE_LINK = "https://stellarburgers.nomoreparties.site/account/profile"  # Страница профиля /profile

    # Составляющие бургера на главной странице
    FILLINGS_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and span[text()='Начинки']]")  # Начинки
    FILLINGS_BUTTON_SELECTED = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') and span[text()='Начинки']]")  # Начинки - Кнопка выделена
    SAUCES_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and span[text()='Соусы']]")  # Соусы
    SAUCES_BUTTON_SELECTED = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') and span[text()='Соусы']]")  # Соусы - Кнопка выделена
    BUNS_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and span[text()='Булки']]")  # Булки
    BUNS_BUTTON_SELECTED = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') and span[text()='Булки']]")  # Булки - Кнопка выделена
