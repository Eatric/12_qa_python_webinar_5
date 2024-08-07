from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
from helpers import Help
from locators import MestoLocators


class TestMestoLogin:

    def test_login(self, driver):
        # AAA
        generated_email = Help.generate_email()

        email_input = driver.find_element(*MestoLocators.LOGIN_INPUT_FIELD)
        email_input.send_keys(generated_email)

        password_input = driver.find_element(*MestoLocators.PASSWORD_INPUT_FIELD)
        password_input.send_keys(Data.AUTH_PASSWORD)

        submit_button = driver.find_element(*MestoLocators.LOGIN_SUBMIT_BUTTON)
        submit_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(MestoLocators.PROFILE_TITLE))

        profile_title = driver.find_element(*MestoLocators.PROFILE_TITLE)
        assert profile_title.is_displayed()


