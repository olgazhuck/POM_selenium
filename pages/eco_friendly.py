from selenium.webdriver.support.ui import WebDriverWait
from utils import project_ec
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from pages.locators import eco_page_locators as loc


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    # def __init__(self, driver):
    #     self.driver = driver

    def add_to_cart_eco(self, text):
        item = self.driver.find_element(*loc.ana_shorts_locator)
        add_to_cart = self.driver.find_element(*loc.add_to_cart_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(item)
        actions.perform()
        actions.move_to_element(add_to_cart)
        actions.click()
        actions.perform()
        product_title_locator = loc.ana_short_product_title_locator
        WebDriverWait(self.driver, 10).until(
            project_ec.text_is_not_empty_in_element(product_title_locator)
            )
        element = self.driver.find_element(*product_title_locator)
        assert element.text == text, "Item not found"

    def check_material_eco(self, text):
        option = self.driver.find_element(*loc.material_menu_locator)
        option.click()
        spandex_option = loc.spandex_locator
        WebDriverWait(self.driver, 10).until(
            project_ec.text_is_not_empty_in_element(spandex_option)
            )
        menu_element = self.driver.find_element(*spandex_option)
        menu_element.click()
        product_element_locator = loc.fiona_shorts_locator
        WebDriverWait(self.driver, 10).until(
            project_ec.text_is_not_empty_in_element(product_element_locator)
            )
        element = self.driver.find_element(*product_element_locator)
        assert element.text == text, "Spandex short not found"

    def wish_list(self, text):
        item = self.driver.find_element(*loc.ana_shorts_locator)
        add_to_wish_list = self.driver.find_element(*loc.add_to_wish_list)
        actions = ActionChains(self.driver)
        actions.move_to_element(item)
        actions.perform()
        actions.move_to_element(add_to_wish_list)
        actions.click(add_to_wish_list)
        actions.perform()
        customer_login = loc.customer_login_locator
        WebDriverWait(self.driver, 10).until(
            project_ec.text_is_not_empty_in_element(customer_login)
            )
        element = self.driver.find_element(*customer_login)
        assert element.text == text, "Item not found"
