import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators


class TestNavigation:

    def test_constructor_navigation_tabs(self, driver):
        driver.find_element(*TestLocators.TAB_SAUCES).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.TITLE_SAUCES_TEXT))
        driver.find_element(*TestLocators.TAB_FILLING).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.TITLE_FILLING_TEXT))
        driver.find_element(*TestLocators.TAB_BUNS).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.TITLE_BUNS_TEXT))

    def test_constructor_navigation_personal_account(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.AUTHORIZATION_TITLE_TEXT))
        assert driver.find_element(*TestLocators.REGISTRATION_TEXT).is_displayed()

    @pytest.mark.parametrize(
        "locator",
        [
            TestLocators.NAVIGATION_CONSTRUCTOR_TEXT,
            TestLocators.NAVIGATION_CONSTRUCTOR_IMAGE
        ]
    )
    def test_navigation_personal_account_navigation_constructor(self, driver, locator):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.AUTHORIZATION_TITLE_TEXT))
        driver.find_element(*locator).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.ASSEMBLE_BURGER_TEXT))
        assert  driver.find_element(*TestLocators.TITLE_BUNS_TEXT).is_displayed()
