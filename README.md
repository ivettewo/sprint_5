# Список тестов:
- test_registration_valid_data_success.py - Успешная регистрация.
- test_registration_short_password_error.py - Ошибка для некорректного пароля, то есть для короткого пароля.
- test_login_from_forgot_password_page.py - Вход через кнопку в форме восстановления пароля.
- test_login_from_register_page.py - Вход через кнопку в форме регистрации.
- test_login_success.py - Вход по кнопке «Войти в аккаунт» на главной.
- test_login_through_personal_account.py - Вход через кнопку «Личный кабинет».
- test_personal_account_redirect_if_authorized.py - Переход в личный кабинет если авторизован
- test_personal_account_redirect_if_not_authorized.py - Переход в личный кабинет если не авторизован *
- test_navigate_from_account_to_constructor.py - Переход из аккаунта по клику на кнопку «Конструктор».
- test_navigate_from_account_to_home_via_logo.py - Переход из аккаунта по клику на логотип Stellar Burgers.
- test_logout_from_account.py - Выход из аккаунта по кнопке «Выйти» в личном кабинете

- test_navigate_between_tabs_selected.py - переходы к разделам: «Булки», «Соусы», «Начинки».

# Фикстуры:
- random_word - Генератор случайного слова. Диапазон от 6 до 8. Нижний регистр + цифры
- random_short_password - Как и random_word, только меньший диапазон, от 1 до 5
- static_data - Статическая дата
- driver
- get_element - Получаем элемент. Встроен WebDriverWait