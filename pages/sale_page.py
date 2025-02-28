import pytest_check as check
from pages.base_page import BasePage
from pages.locators import sale_page_locators as sale


class SalePage(BasePage):
    page_url = '/sale.html'

    def check_deals(self, text, locator):
        deal_title = self.driver.find_element(*locator)
        check.equal(
            deal_title.text, text, f"No {text} in {locator} element on Sale page"
            )

    def check_menu(self, text, locator):
        header_title = self.driver.find_element(*locator)
        check.equal(header_title.text, text, f"No such text in {locator[1]}")

    def check_women_deals(self, text):
        self.check_deals(text, sale.women_deals_locator)

    def check_men_deals(self, text):
        self.check_deals(text, sale.men_deals_locator)
    
    def check_gear_deals(self, text):
        self.check_deals(text, sale.gear_deals_locator)

    def check_women_menu_sweaters(self, text):
        self.check_menu(text, sale.women_hoodies_locator)

    def check_women_menu_jackets(self, text):
        self.check_menu(text, sale.women_jackets_locator)

    def check_women_menu_pants(self, text):
        self.check_menu(text, sale.women_pants_locator)

    def check_women_menu_shorts(self, text):
        self.check_menu(text, sale.women_shorts_locator)

    def check_hoodies_deal(self, text):
        hoodie_locator = (sale.women_hoodies_locator)
        self.driver.find_element(*hoodie_locator).click()
        header = (sale.h1)
        header_text = self.driver.find_element(*header)
        assert header_text.text == text, f"No {text} in {hoodie_locator}"
