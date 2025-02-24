from pages.locators import create_acc_locators as loc
from pages.locators import sale_page_locators as sale


# create account tests
def test_create_account_with_invalid_email(create_new_customer):
    create_new_customer.open_page()
    create_new_customer.fill_create_account_form(
        "Bob", "Marley", "bob", "1234567890Qw!", "1234567890Qw!"
    )
    create_new_customer.check_error_alert_invalid_email(
        'Please enter a valid email address (Ex: johndoe@domain.com).'
    )


def test_header_title_text(create_new_customer):
    create_new_customer.open_page()
    create_new_customer.check_page_header_is('Create New Customer Account')


def test_wrong_confirm_password(create_new_customer):
    create_new_customer.open_page()
    create_new_customer.fill_create_account_form(
        "Bob", "Marley", "bob@hj.vh", "1234567890Qw!", "1234567890Qw"
    )
    create_new_customer.check_error_alert_wrong_confirm_password(
        'Please enter the same value again.'
    )


def test_validation_messages_empty_fields(create_new_customer):
    validation_text = 'This is a required field.'
    create_new_customer.open_page()
    create_new_customer.fill_create_account_form(
        "", "", "", "", ""
    )
    create_new_customer.check_required_empty_fields(
        validation_text, loc.first_name_error_locator
    )
    create_new_customer.check_required_empty_fields(
        validation_text, loc.last_name_error_locator
    )
    create_new_customer.check_required_empty_fields(
        validation_text, loc.email_error_locator
    )
    create_new_customer.check_required_empty_fields(
        validation_text, loc.password_error_locator
    )
    create_new_customer.check_required_empty_fields(
        validation_text, loc.confirm_password_error_locator
    )


# Sales page tests
def test_header_title(sale_page):
    sale_page.open_page()
    sale_page.check_deals("Women's Deals", sale.women_deals_locator)
    sale_page.check_deals("Mens's Deals", sale.men_deals_locator)
    sale_page.check_deals("Gear Deals", sale.gear_deals_locator)


def test_women_menu_items(sale_page):
    sale_page.open_page()
    sale_page.check_deals(
        "Hoodies and Sweatshirts", sale.women_hoodies_locator
        )
    sale_page.check_deals("Jackets", sale.women_jackets_locator)
    sale_page.check_deals("Tees", sale.women_tees_locator)
    sale_page.check_deals("Bras & Tanks", sale.women_bra_locator)
    sale_page.check_deals("Pants", sale.women_pants_locator)
    sale_page.check_deals("Shorts", sale.women_shorts_locator)


def test_hoodies_deal(sale_page):
    sale_page.open_page()
    sale_page.check_menu(
        "Hoodies & Sweatshirts", sale.women_hoodies_locator, sale.h1
        )


# eco friendly tests
def test_add_to_cart(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.add_to_cart_eco('Ana Running Short')


def test_product_page_opened(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.check_material_eco('Fiona Fitness Short')


def test_add_to_wish_list(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.wish_list('Customer Login')
