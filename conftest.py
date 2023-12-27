import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constant
from locators import Locator


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Constant.MAIN_URL)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def entry_on_page_reg(driver):
    driver.find_element(*Locator.BUTTON_ACC).click()  # переход на страницу входа в аккаунт
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(Locator.LINK_REG)
    )
    driver.find_element(*Locator.LINK_REG).click()  # переход на страницу регистрации
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locator.BUTTON_GET_REG)
    )
    return driver


@pytest.fixture
def auth(driver):
    driver.find_element(*Locator.BUTTON_ACC).click()  # переход на страницу входа в аккаунт
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(Locator.LINK_REG)
    )
    driver.find_element(*Locator.EMAIL_FIELD).send_keys(
        Constant.TEST_USER_EMAIL
    )
    driver.find_element(*Locator.PASSWORD_FIELD).send_keys(
        Constant.TEST_USER_PASSWORD
    )
    driver.find_element(*Locator.BUTTON_INTO).click()  # переход на главную страницу
    return driver


@pytest.fixture
def log_out(driver, auth):
    driver.find_element(*Locator.BUTTON_ACC).click()  # переход на страницу личного кабинета
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locator.BUTTON_LOG_OUT)
    )
    driver.find_element(*Locator.BUTTON_LOG_OUT).click()  # переход на страницу входа в аккаунт
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locator.LOGO))
    driver.find_element(*Locator.LOGO).click()  # переход на главную страницу
    return driver
