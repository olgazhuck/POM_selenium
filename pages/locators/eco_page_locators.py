from selenium.webdriver.common.by import By

# deals locators
ana_shorts_locator = (By.XPATH, "(//div[@class='product-item-info'])[1]")
add_to_cart_locator = (
        By.XPATH, """
        //button[
        @type='submit' and @title='Add to Cart' and contains(@class, 'tocart')
        ]
        """
    )
ana_short_product_title_locator = (
        By.XPATH, """
        //span[
            @class='base' and
            @data-ui-id='page-title-wrapper' and
            @itemprop='name'
        ]
        """
    )
material_menu_locator = (
        By.XPATH, "//div[@data-role='title' and text()='Material']"
    )
spandex_locator = (
        By.XPATH, """
        //li[@class='item']/a[text()[normalize-space()='Spandex']]
        """
    )
fiona_shorts_locator = (
        By.XPATH, """
        //a[
        @class='product-item-link' and normalize-space()='Fiona Fitness Short'
        ]
        """
    )
add_to_wish_list = (
        By.XPATH, """
        //a[@class='action towishlist' and @title='Add to Wish List']
        """
    )
customer_login_locator = (
        By.XPATH, """
        //span[@class='base' and contains(text(), 'Customer Login')]
        """
    )
