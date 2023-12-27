from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constant
from locators import Locator

faker = Faker()


class TestRegistration:
    def test_registration_success(self, driver, entry_on_page_reg):
        name = faker.name()
        email = faker.email()
        password = Constant.TEST_USER_PASSWORD
        driver.find_element(*Locator.NAME_FIELD_REG).send_keys(name)
        driver.find_element(*Locator.EMAIL_FIELD_REG).send_keys(email)
        driver.find_element(*Locator.PASSWORD_FIELD_REG).send_keys(password)
        driver.find_element(*Locator.BUTTON_GET_REG).click()  # переход на страницу входа в аккаунт
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locator.BUTTON_INTO)
        )
        driver.find_element(*Locator.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locator.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locator.BUTTON_INTO).click()  # переход на главную страницу
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locator.BUTTON_ACC)
        )
        driver.find_element(*Locator.BUTTON_ACC).click()  # переход на страницу личного кабинета
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locator.BUTTON_PROFILE)
        )
        assert driver.find_element(*Locator.NAME_FIELD).get_attribute('value') == name

    def test_registration_not_valid_len_password_error(
            self, driver, entry_on_page_reg):
        name = faker.name()
        email = faker.email()
        password = Constant.UNCORRECT_PASSWORD
        driver.find_element(*Locator.NAME_FIELD_REG).send_keys(name)
        driver.find_element(*Locator.EMAIL_FIELD_REG).send_keys(email)
        driver.find_element(*Locator.PASSWORD_FIELD_REG).send_keys(password)
        driver.find_element(*Locator.BUTTON_GET_REG).click()  # переход на страницу входа в аккаунт
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locator.LABEL_UNCORRECT_PASSWORD)
        )
