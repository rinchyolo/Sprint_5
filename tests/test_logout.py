from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import *
from locators import TestLocators


class TestLogout:

    def test_logout_after_successful_login(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(LOGIN)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*TestLocators.AUTHORIZATION_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.ASSEMBLE_BURGER_TEXT))
        # Проверка, что данные пользователя совпадают при регистрации
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.PASSWORD_INPUT))
        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.AUTHORIZATION_TITLE_TEXT))
