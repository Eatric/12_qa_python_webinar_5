from selenium.webdriver.common.by import By


class MestoLocators:
    LOGIN_INPUT_FIELD = (By.XPATH, "//input[@placeholder='Email']")
    PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@placeholder='Пароль']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text() = 'Войти']")

    PROFILE_TITLE = (By.XPATH, "//h1[@class = 'profile__title']")
