from selenium.webdriver.common.by import By

from locators import Locators


class TestCategories:
    def test_click_bun(self, driver_init):
        assert driver_init.find_element(By.XPATH, Locators.bun_button).is_displayed() is True

    def test_click_sauces(self, driver_init):
        assert driver_init.find_element(By.XPATH, Locators.sauces_button).is_displayed() is True

    def test_click_fillings(self, driver_init):
        assert driver_init.find_element(By.XPATH, Locators.fillings_button).is_displayed() is True
