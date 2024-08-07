import pytest
from selenium import webdriver


URL = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture(scope='function')
def driver_init():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()
