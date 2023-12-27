from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locator


class TestLogOut:
    def test_log_out_by_button_on_acc_page_success(self, driver, auth):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locator.BUTTON_ACC)
        )
        driver.find_element(*Locator.BUTTON_ACC).click()  # переход на страницу личного кабинета
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locator.BUTTON_LOG_OUT)
        )
        driver.find_element(*Locator.BUTTON_LOG_OUT).click()  # переход на страницу входа в аккаунт
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locator.LOGO)
        )
        driver.find_element(*Locator.LOGO).click()  # переход на главную страницу
        driver.find_element(*Locator.BUTTON_ACC).click()  # переход на страницу личного кабинета
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locator.BUTTON_INTO)
        )
