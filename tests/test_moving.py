from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locator


class TestMoving:
    def test_moving_in_acc_by_button_on_header_success(self, driver, auth):
        driver.find_element(*Locator.BUTTON_ACC).click()  # переход на страницу личного кабинета
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locator.BUTTON_PROFILE)
        )

    def test_moving_on_main_page_by_button_on_header_success(self, driver, auth):
        driver.find_element(*Locator.BUTTON_ACC).click()  # переход на страницу личного кабинета
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locator.BUTTON_PROFILE)
        )
        driver.find_element(*Locator.BUTTON_CONSTR).click()  # переход на главную страницу
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locator.TITLE_GATHER_BURGER)
        )

    def test_moving_on_main_page_by_logo_on_header_success(self, driver, auth):
        driver.find_element(*Locator.BUTTON_ACC).click()  # переход на страницу личного кабинета
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locator.BUTTON_PROFILE)
        )
        driver.find_element(*Locator.LOGO).click()  # переход на главную страницу
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locator.TITLE_GATHER_BURGER)
        )
