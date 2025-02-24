from selenium.webdriver.common.by import By

# deals locators
women_deals_locator = (By.XPATH, "(//strong[@class='title']/span)[1]")
men_deals_locator = (By.XPATH, "(//strong[@class='title']/span)[2]")
gear_deals_locator = (By.XPATH, "(//strong[@class='title']/span)[3]")
# women's deals locators
women_hoodies_locator = (By.XPATH, "//li[@class='item']/a[1]")
women_jackets_locator = (By.XPATH, "(//li[@class='item']/a)[2]")
women_tees_locator = (By.XPATH, "(//li[@class='item']/a)[3]")
women_bra_locator = (By.XPATH, "(//li[@class='item']/a)[4]")
women_pants_locator = (By.XPATH, "(//li[@class='item']/a)[5]")
women_shorts_locator = (By.XPATH, "(//li[@class='item']/a)[6]")
# headers
h1 = (By.TAG_NAME, 'h1')
