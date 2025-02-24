import pytest
from selenium import webdriver
from pages.sale_page import SalePage
from pages.create_new_customer import CreateNewCustomer
from pages.eco_friendly import EcoFriendlyPage

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def create_new_customer(driver):
    return CreateNewCustomer(driver)


@pytest.fixture()
def eco_friendly(driver):
    return EcoFriendlyPage(driver)

