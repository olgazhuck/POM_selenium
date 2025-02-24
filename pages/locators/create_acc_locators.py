from selenium.webdriver.common.by import By


firstname_field_loc = (By.ID, 'firstname')
lastname_field_loc = (By.ID, 'lastname')
email_field_loc = (By.ID, 'email_address')
password_field_loc = (By.ID, 'password')
password_confirmation_field_loc = (By.ID, 'password-confirmation')
buttom_create_acc_loc = (
            By.XPATH,  "//button[@title='Create an Account']"
            )
error_locator_loc = (
            By.ID, "email_address-error"
            )
header_loc = (By.TAG_NAME, 'h1')
confirm_password_locator = (
    By.ID, 'password-confirmation-error'
)

# error locators
first_name_error_locator = (By.ID, 'firstname-error')
last_name_error_locator = (By.ID, 'lastname-error')
email_error_locator = (By.ID, 'email_address-error')
password_error_locator = (By.ID, 'password-error')
confirm_password_error_locator = (By.ID, 'password-confirmation-error')
