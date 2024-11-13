import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import *
from locators import TestLocators


class TestAuthorization:

    @pytest.mark.parametrize(
        "locator",
        [
            TestLocators.PERSONAL_ACCOUNT,
            TestLocators.AUTHORIZATION_MAIN_BUTTON
        ]
    )
    def test_authorization_via_personal_account_and_main_button(self, driver, locator):
        driver.find_element(*locator).click()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(LOGIN)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*TestLocators.AUTHORIZATION_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.ASSEMBLE_BURGER_TEXT))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.PASSWORD_INPUT))
        assert driver.find_element(*TestLocators.LOGIN_INPUT).get_attribute('value') == LOGIN
        assert driver.find_element(*TestLocators.NAME_INPUT).get_attribute('value') == NAME

    @pytest.mark.parametrize(
        "locator",
        [
            TestLocators.REGISTRATION_TEXT,
            TestLocators.RECOVERY_PASSWORD_TEXT
        ]
    )
    def test_authorization_via_registration_and_password_recovery(self, driver, locator):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        driver.find_element(*locator).click()
        driver.find_element(*TestLocators.AUTHORIZATION_TEXT).click()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(LOGIN)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*TestLocators.AUTHORIZATION_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.ASSEMBLE_BURGER_TEXT))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.PASSWORD_INPUT))
        assert driver.find_element(*TestLocators.LOGIN_INPUT).get_attribute('value') == LOGIN
        assert driver.find_element(*TestLocators.NAME_INPUT).get_attribute('value') == NAME
