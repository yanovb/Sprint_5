from selenium.webdriver.support import expected_conditions
from generator import *
from locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from test_data import INVALID_PASSWORD


class TestRegistration:
    def test_registration_valid_data_successful(self, driver_init):
        driver_init.find_element(By.XPATH, Locators.personal_account_button).click()
        driver_init.find_element(By.XPATH, Locators.registration_init_button).click()
        driver_init.find_element(By.XPATH, Locators.name_field).send_keys(password_or_name_generator())
        driver_init.find_element(By.XPATH, Locators.email_field).send_keys(mail_generator())
        driver_init.find_element(By.XPATH, Locators.password_field).send_keys(password_or_name_generator())
        driver_init.find_element(By.XPATH, Locators.registration_button).click()
        elm = Locators.the_inscription_entrance
        WebDriverWait(driver_init, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, elm)))
        assert driver_init.find_element(By.XPATH, elm).text == 'Вход'

    def test_registration_invalid_password_unsuccessfully(self, driver_init):
        driver_init.find_element(By.XPATH, Locators.personal_account_button).click()
        driver_init.find_element(By.XPATH, Locators.registration_init_button).click()
        driver_init.find_element(By.XPATH, Locators.name_field).send_keys(password_or_name_generator())
        driver_init.find_element(By.XPATH, Locators.email_field).send_keys(mail_generator())
        driver_init.find_element(By.XPATH, Locators.password_field).send_keys(INVALID_PASSWORD)
        driver_init.find_element(By.XPATH, Locators.registration_button).click()
        result = driver_init.find_element(By.XPATH, Locators.the_inscription_incorrect_password).text
        assert result == 'Некорректный пароль'
