from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locator


class TestConstrMoving:
    def test_moving_to_buns_by_label_in_constr_success(self, driver):
        driver.maximize_window()
        driver.find_element(*Locator.LABEL_SAUCES).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.TITLE_SAUCES)
        )
        driver.find_element(*Locator.LABEL_BUNS).click()
        assert WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locator.TITLE_BUNS)
        )

    def test_moving_to_fillings_by_label_in_constr_success(self, driver):
        driver.find_element(*Locator.LABEL_FILLINGS).click()
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locator.TITLE_FILLINGS)
        )

    def test_moving_to_sauces_by_label_in_constr_success(self, driver):
        driver.find_element(*Locator.LABEL_SAUCES).click()
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locator.TITLE_SAUCES)
        )
