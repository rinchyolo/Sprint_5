from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import *
from helpers import generate_login
from locators import TestLocators


class TestRegistration:

    def test_registration_wrong_password(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.REGISTRATION_TEXT).click()
        driver.find_element(*TestLocators.NAME_INPUT).send_keys(NAME)
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(generate_login())
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(WRONG_PASSWORD)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element(TestLocators.INVALID_PASSWORD_TEXT,
                                                              INVALID_PASSWORD_MESSAGE))
        assert driver.find_element(*TestLocators.INVALID_PASSWORD_TEXT).is_displayed()

    def test_registration_success(self, driver):
        # Регистрация пользователя
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.REGISTRATION_TEXT).click()
        driver.find_element(*TestLocators.NAME_INPUT).send_keys(NAME)
        email = generate_login()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        # Авторизация пользователя
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.AUTHORIZATION_TITLE_TEXT))
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*TestLocators.AUTHORIZATION_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.ASSEMBLE_BURGER_TEXT))
        # Проверка, что данные пользователя совпадают при регистрации
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.PASSWORD_INPUT))
        assert driver.find_element(*TestLocators.LOGIN_INPUT).get_attribute('value') == email
        assert driver.find_element(*TestLocators.NAME_INPUT).get_attribute('value') == NAME
