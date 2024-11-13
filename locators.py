from selenium.webdriver.common.by import By


class TestLocators:
    # Локаторы для регистрации
    PERSONAL_ACCOUNT = [By.XPATH, '//*[text()="Личный Кабинет"]']  # Личный кабинет
    REGISTRATION_TEXT = [By.XPATH, '//*[text()="Зарегистрироваться"]']  # Текст "Зарегистрироваться"
    NAME_INPUT = [By.XPATH, '//label[text()="Имя"]/following-sibling::input']  # Поле для ввода имени
    EMAIL_INPUT = [By.XPATH, '//label[text()="Email"]/following-sibling::input']  # Поле для ввода почты
    PASSWORD_INPUT = [By.XPATH, '//label[text()="Пароль"]/following-sibling::input']  # Поле для ввода пароля
    LOGIN_INPUT = [By.XPATH, '//label[text()="Логин"]/following-sibling::input']  # Поле для ввода логина
    REGISTRATION_BUTTON = [By.XPATH, '//button[text()="Зарегистрироваться"]']  # Кнопка "Зарегистрироваться"
    INVALID_PASSWORD_TEXT = [By.XPATH, '//p[contains(@class, "input__error")]']  # Текст с ошибкой при регистрации
    AUTHORIZATION_TITLE_TEXT = [By.XPATH, '//h2[text()="Вход"]']  # Заголовок "Вход"
    AUTHORIZATION_BUTTON = [By.XPATH, '//button[text()="Войти"]']  # Кнопка "Войти"
    ASSEMBLE_BURGER_TEXT = [By.XPATH, '//h1[text()="Соберите бургер"]']  # Текст "Соберите бургер"
    AUTHORIZATION_MAIN_BUTTON = [By.XPATH,
                                 '//button[text()="Войти в аккаунт"]']  # Кнопка "Войти в аккаунт" на главной странице
    AUTHORIZATION_TEXT = [By.XPATH, '//a[text()="Войти"]']  # Текст "Войти"
    RECOVERY_PASSWORD_TEXT = [By.XPATH, '//*[text()="Зарегистрироваться"]']  # Текст "Восстановить пароль"
    LOGOUT_BUTTON = [By.XPATH, '//button[text()="Выход"]']  # Кнопка "Выход"
    TAB_SAUCES = [By.XPATH, '//div[contains(@class, "tab")]/span[text()="Соусы"]']  # Таб "Соусы"
    TITLE_SAUCES_TEXT = [By.XPATH, '//div[contains(@class, "BurgerIngredients")]/h2[text()="Соусы"]']  # Тайтл "Соусы"
    TAB_FILLING = [By.XPATH, '//div[contains(@class, "tab")]/span[text()="Начинки"]']  # Таб "Начинки"
    TITLE_FILLING_TEXT = [By.XPATH,
                          '//div[contains(@class, "BurgerIngredients")]/h2[text()="Начинки"]']  # Тайтл "Начинки"
    TAB_BUNS = [By.XPATH, '//div[contains(@class, "tab")]/span[text()="Булки"]']  # Таб "Булки"
    TITLE_BUNS_TEXT = [By.XPATH,
                       '//div[contains(@class, "BurgerIngredients")]/h2[text()="Булки"]']  # Тайтл "Булки"
    NAVIGATION_CONSTRUCTOR_TEXT = [By.XPATH,
                                   '//nav[contains(@class, "AppHeader_header")]//p[text()="Конструктор"]']  # Текст навигационного таба "Конструктор"
    NAVIGATION_CONSTRUCTOR_IMAGE = [By.XPATH,
                                    '//p[text()="Конструктор"]/preceding::*']  # Картинка навигационного таба "Конструктор"
