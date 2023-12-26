from selenium.webdriver.common.by import By


class Locator:
    # Элементы хедера
    BUTTON_ACC = (By.CSS_SELECTOR, "header a[href='/account']")  # Кнопка "Личный кабинет"
    LOGO = (
        By.CSS_SELECTOR, "header div[class='AppHeader_header__logo__2D0X2']"
    )  # Логотип "Stellar Burgers"
    BUTTON_CONSTR = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # Кнопка "Конструктор"

    # Элементы на главной странице
    BUTTON_INTO_ACC = (
        By.XPATH, "//main/section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']/div/button"
    )  # Кнопка "Войти в аккаунт"
    BUTTON_GET_ORDER = (By.XPATH, "//main/section[2]/div/button")  # Кнопка "Оформить заказ"
    TITLE_GATHER_BURGER = (
        By.XPATH, "//main/section[1]/h1[@class='text text_type_main-large mb-5 mt-10']"
    )  # Заголовок "Соберите бургер"

    # Элементы контруктора
    LABEL_BUNS = (By.XPATH, "//main/section[1]/div[1]/div[1]")  # Надпись "Булки" над скроллом
    LABEL_SAUCES = (By.XPATH, "//main[1]/section[1]/div[1]/div[2]")  # Надпись "Соусы" над скроллом
    LABEL_FILLINGS = (By.XPATH, "//main[1]/section[1]/div[1]/div[3]")  # Надпись "Начинки" над скроллом
    TITLE_BUNS = (By.XPATH, "//main/section[1]/div[2]/h2[1]")  # Заголовок "Булки"
    TITLE_SAUCES = (By.XPATH, "//main/section[1]/div[2]/h2[2]")  # Заголовок "Соусы"
    TITLE_FILLINGS = (By.XPATH, "//main/section[1]/div[2]/h2[3]")  # Заголовок "Начинки"

    # Элементы на странице регистрации
    NAME_FIELD_REG = (By.XPATH, "//fieldset[1]/div/div/input")  # Поле ввода "Имя"
    EMAIL_FIELD_REG = (By.XPATH, "//fieldset[2]/div/div/input")  # Поле ввода "Email"
    PASSWORD_FIELD_REG = (By.CSS_SELECTOR, "fieldset input[type='password']")  # Поле ввода "Пароль"
    BUTTON_GET_REG = (By.XPATH, "//main/div/form/button")  # Кнопка "Зарегистрироваться"
    LABEL_UNCORRECT_PASSWORD = (
        By.CSS_SELECTOR, "form p[class='input__error text_type_main-default']"
    )  # Надпись "Некорректный пароль" под полем ввода пароля

    # Элементы на странице входа в аккаунт
    EMAIL_FIELD = (By.CSS_SELECTOR, "fieldset input[type='text']")  # Поле ввода "Email"
    PASSWORD_FIELD = (By.CSS_SELECTOR, "fieldset input[type='password']")  # Поле ввода "Пароль"
    BUTTON_INTO = (By.XPATH, "//button[contains(text(),'Войти')]")  # Кнопка "Войти"
    LINK_REG = (By.CSS_SELECTOR, "main p a[href = '/register']")  # Ссылка "Зарегистрироваться"
    LINK_RECOV_PASS = (By.CSS_SELECTOR, "main p a[href = '/forgot-password']")  # Ссылка "Восстановить пароль"

    # Элементы на странице личного кабинета
    BUTTON_PROFILE = (By.CSS_SELECTOR, "main nav a[href='/account/profile']")  # Ссылка "Профиль"
    BUTTON_LOG_OUT = (By.CSS_SELECTOR, "main nav button")  # Кнопка "Выход"
    NAME_FIELD = (By.XPATH, "//main/div/div/div/ul/li[1]/div/div/input")  # Поле "Имя"

    # Элементы на странице восстановления пароля
    BUTTON_INTO_ON_RECOV_PASS_PAGE = (By.CSS_SELECTOR, "main a[href='/login']")  # Ссылка "Войти"
