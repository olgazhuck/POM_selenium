from pages.base_page import BasePage


class SalePage(BasePage):
    page_url = '/sale.html'

    def check_deals(self, text, locator):
        deal_title = self.driver.find_element(*locator)
        assert deal_title.text == text, \
            f"No such text in {locator} element on Sale page"

    def check_menu(self, text, menu_item, locator):
        menu_item = self.driver.find_element(*menu_item)
        menu_item.click()
        header_title = self.driver.find_element(*locator)
        assert header_title.text == text, "No such text"
