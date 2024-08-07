from selenium.webdriver.common.by import By
from locators import Locators


class TestSwitchingToConstructor:
    def test_switching_using_constructor_button(self, driver_init):
        driver_init.find_element(By.XPATH, Locators.personal_account_button).click()
        driver_init.find_element(By.XPATH, Locators.constructor_button).click()
        assert driver_init.find_element(By.XPATH, Locators.constructor_inscription).text == 'Соберите бургер'

    def test_switching_using_logo(self, driver_init):
        driver_init.find_element(By.XPATH, Locators.personal_account_button).click()
        driver_init.find_element(By.XPATH, Locators.button_on_logo).click()
        assert driver_init.find_element(By.XPATH, Locators.constructor_inscription).text == 'Соберите бургер'
