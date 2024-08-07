from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from test_data import *


class TestPersonalAccount:
    def test_personal_account(self, driver_init):
        driver_init.find_element(By.XPATH, Locators.personal_account_button).click()
        driver_init.find_element(By.XPATH, Locators.email_field).send_keys(EMAIL)
        driver_init.find_element(By.XPATH, Locators.password_field).send_keys(PASSWORD)
        driver_init.find_element(By.XPATH, Locators.authorization_button).click()
        elm = Locators.personal_account_button
        WebDriverWait(driver_init, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, elm)))
        driver_init.find_element(By.XPATH, Locators.personal_account_button).click()
        elm = Locators.disabled_login
        WebDriverWait(driver_init, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, elm)))
        assert driver_init.find_element(By.XPATH, Locators.disabled_login).get_attribute('value') == LOGIN
