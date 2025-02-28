from selenium.webdriver.support.ui import WebDriverWait
from utils import project_ec
from pages.locators import create_acc_locators as loc


class CreateNewCustomer:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(
            'https://magento.softwaretestingboard.com/customer/account/create/'
            )

    def fill_create_account_form(
            self, firstname, lastname, email, password, password_confirmation
            ):
        firstname_field = self.driver.find_element(*loc.firstname_field_loc)
        lastname_field = self.driver.find_element(*loc.lastname_field_loc)
        email_field = self.driver.find_element(*loc.email_field_loc)
        password_field = self.driver.find_element(*loc.password_field_loc)
        password_confirmation_field = self.driver.find_element(
            *loc.password_confirmation_field_loc
            )
        firstname_field.send_keys(firstname)
        lastname_field.send_keys(lastname)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_confirmation_field.send_keys(password_confirmation)
        button_create_acc = self.driver.find_element(
            *loc.buttom_create_acc_loc
            )
        button_create_acc.click()

    def check_error_alert_invalid_email(self, text):
        error_locator = (
            loc.error_locator_loc
            )
        error_message = self.driver.find_element(*error_locator)
        WebDriverWait(self.driver, 10).until(
            project_ec.text_is_not_empty_in_element(error_locator)
            )
        assert error_message.text == text, "Email validation is not working"

    def check_error_alert_wrong_confirm_password(self, text):
        error_locator = (
            loc.confirm_password_locator
            )
        error_message = self.driver.find_element(*error_locator)
        WebDriverWait(self.driver, 10).until(
            project_ec.text_is_not_empty_in_element(error_locator)
            )
        assert error_message.text == text, "Email validation is not working"

    def check_page_header_is(self, text):
        header_title = self.driver.find_element(*loc.header_loc)
        assert header_title.text == text, \
            'No "Create New Customer Account" text'

    def check_empty_field_firstname(self, text):
        error_locator = (
            loc.first_name_error_locator
            )
        error_message = self.driver.find_element(*error_locator)
        WebDriverWait(self.driver, 10).until(
            project_ec.text_is_not_empty_in_element(error_locator)
            )
        assert error_message.text == text, "First Name error doesn't show"

    def check_empty_field_lasttname(self, text):
        error_locator = (
            loc.first_name_error_locator
            )
        error_message = self.driver.find_element(*error_locator)
        WebDriverWait(self.driver, 10).until(
            project_ec.text_is_not_empty_in_element(error_locator)
            )
        assert error_message.text == text, "Last Name error doesn't show"

    def check_required_empty_fields(self, validation_text, locator):
        error_message = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 10).until(
            project_ec.text_is_not_empty_in_element(locator)
            )
        assert error_message.text == validation_text, \
            f"Field {locator[1]} has no validation message"

    def check_first_name_empty_validation_text(self, validation_text):
        self.check_required_empty_fields(
            validation_text, loc.first_name_error_locator
            )

    def check_last_name_empty_validation_text(self, validation_text):
        self.check_required_empty_fields(
            validation_text, loc.last_name_error_locator
            )

    def check_email_empty_validation_text(self, validation_text):
        self.check_required_empty_fields(
            validation_text, loc.email_error_locator
            )

    def check_password_validation_text(self, validation_text):
        self.check_required_empty_fields(
            validation_text, loc.password_error_locator
            )

    def check_confirm_password_validation_text(self, validation_text):
        self.check_required_empty_fields(
            validation_text, loc.confirm_password_error_locator
            )
