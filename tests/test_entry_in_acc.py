from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constant
from locators import Locator


class TestEntry:
    def test_entry_in_acc_by_button_on_main_page_entry_success(
            self, driver, log_out):
        driver.find_element(*Locator.BUTTON_INTO_ACC).click()  # переход на страницу личного кабинета
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locator.BUTTON_INTO)
        )
        driver.find_element(*Locator.EMAIL_FIELD).send_keys(
            Constant.TEST_USER_EMAIL)
        driver.find_element(*Locator.PASSWORD_FIELD).send_keys(
            Constant.TEST_USER_PASSWORD)
        driver.find_element(*Locator.BUTTON_INTO).click()  # переход на главную страницу
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locator.BUTTON_ACC)
        )
        driver.find_element(*Locator.BUTTON_ACC).click()  # переход на страницу личного кабинета
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locator.BUTTON_PROFILE)
        )
        assert driver.find_element(*Locator.NAME_FIELD).get_attribute('value') == Constant.TEST_USER_NAME

    def test_entry_in_acc_by_button_on_header_entry_success(
            self, driver, log_out):
        driver.find_element(*Locator.BUTTON_ACC).click()  # переход на страницу личного кабинета
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locator.BUTTON_INTO)
        )
        driver.find_element(*Locator.EMAIL_FIELD).send_keys(
            Constant.TEST_USER_EMAIL)
        driver.find_element(*Locator.PASSWORD_FIELD).send_keys(
            Constant.TEST_USER_PASSWORD)
        driver.find_element(*Locator.BUTTON_INTO).click()  # переход на главную страницу
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locator.BUTTON_ACC)
        )
        driver.find_element(*Locator.BUTTON_ACC).click()  # переход на страницу личного кабинета
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locator.BUTTON_PROFILE)
        )
        assert driver.find_element(*Locator.NAME_FIELD).get_attribute('value') == Constant.TEST_USER_NAME

    def test_entry_in_acc_by_button_on_reg_page_success(self, driver, log_out):
        driver.find_element(*Locator.BUTTON_ACC).click()  # переход на страницу личного кабинета
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locator.BUTTON_INTO)
        )
        driver.find_element(*Locator.EMAIL_FIELD).send_keys(
            Constant.TEST_USER_EMAIL)
        driver.find_element(*Locator.PASSWORD_FIELD).send_keys(
            Constant.TEST_USER_PASSWORD)
        driver.find_element(*Locator.BUTTON_INTO).click()  # переход на главную страницу
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locator.BUTTON_ACC)
        )
        driver.find_element(*Locator.BUTTON_ACC).click()  # переход на страницу личного кабинета
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locator.BUTTON_PROFILE)
        )
        assert driver.find_element(*Locator.NAME_FIELD).get_attribute('value') == Constant.TEST_USER_NAME

    def test_entry_in_acc_by_button_on_recov_pass_page_success(
            self, driver, log_out):
        driver.find_element(*Locator.BUTTON_ACC).click()  # переход на страницу личного кабинета
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locator.BUTTON_INTO)
        )
        driver.find_element(*Locator.LINK_RECOV_PASS).click()  # Переход на страницу восстановления пароля
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locator.BUTTON_INTO_ON_RECOV_PASS_PAGE)
        )
        driver.find_element(*Locator.BUTTON_INTO_ON_RECOV_PASS_PAGE).click()  # переход на страницу входа в аккаунт
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locator.BUTTON_INTO)
        )
        driver.find_element(*Locator.EMAIL_FIELD).send_keys(
            Constant.TEST_USER_EMAIL)
        driver.find_element(*Locator.PASSWORD_FIELD).send_keys(
            Constant.TEST_USER_PASSWORD)
        driver.find_element(*Locator.BUTTON_INTO).click()  # переход на главную страницу
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locator.BUTTON_ACC)
        )
        driver.find_element(*Locator.BUTTON_ACC).click()  # переход на страницу личного кабинета
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locator.BUTTON_PROFILE)
        )
        assert driver.find_element(*Locator.NAME_FIELD).get_attribute('value') == Constant.TEST_USER_NAME
