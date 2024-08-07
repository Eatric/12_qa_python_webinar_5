import pytest
from selenium import webdriver

from data import Data
from helpers import Help


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.chrome()
    chrome_driver.get(Data.MESTO_URL)

    yield chrome_driver

    chrome_driver.quit()


def generated_user():
    return Help.generate_email()
