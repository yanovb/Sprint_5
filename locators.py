from test_data import *


class Locators:
    # кнопка личный кабинет
    personal_account_button = './/a[@href="/account"]'
    # кнопка "Зарегистрироваться" после надписи "Вы — новый пользователь?"
    registration_init_button = './/a[@href="/register"]'
    # поле логина при регистрации
    name_field = './/label[contains(text(),"Имя")]/following-sibling::input'
    # поле почты при регистрации
    email_field = './/label[contains(text(),"Email")]/following-sibling::input'
    # поле пароля при регистрации
    password_field = './/label[contains(text(),"Пароль")]/following-sibling::input'
    # кнопка регистрации в секции регистрации нового пользователя
    registration_button = './/button[contains(text(),"Зарегистрироваться")]'
    # текст Вход
    the_inscription_entrance = './/h2[text()="Вход"]'
    # уведомление о некорректном пароле
    the_inscription_incorrect_password = './/p[text()="Некорректный пароль"]'
    # кнопка авторизации
    authorization_button = './/button[text()="Войти"]'
    # кнопка выхода из авторизованного аккаунта
    exit_button = './/button[text()="Выход"]'
    # поле с указанным логином пользователя
    disabled_login = f'.//input[@value="{LOGIN}"]'
    # кнопка войти в аккаунт на главном экране
    login_button = './/button[text()="Войти в аккаунт"]'
    # кнопка войти в секции регистрации
    the_sign_in_button_in_the_registration_section = './/a[text()="Войти"]'
    # кнопка восстановления пароля
    the_restore_password_button = './/a[text()="Восстановить пароль"]'
    # кнопка авторизации в секции восстановления пароля
    the_login_button_in_the_password_recovery_section = './/a[@href="/login"]'
    # кнопка выхода в констурктор
    constructor_button = './/li/a[@href="/"]'
    # текст соберите бургер
    constructor_inscription = './/h1[text()="Соберите бургер"]'
    # кнопка выхода в констурктор в логотипе
    button_on_logo = './/div[@class="AppHeader_header__logo__2D0X2"]/a'
    # кнопка выхода
    log_out_button = './/button[text()="Выход"]'
    # выбор булок
    bun_button = './/span[text()="Булки"]//parent::*'
    # выбор соусов
    sauces_button = './/span[text()="Соусы"]//parent::*'
    # выбор начинок
    fillings_button = './/span[text()="Начинки"]//parent::*'
