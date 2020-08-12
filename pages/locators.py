from selenium.webdriver.common.by import By

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, "div.basket-mini>span.btn-group>a.btn")

class BasketPageLocators():
    BASKET_URL = "http://selenium1py.pythonanywhere.com/en-gb/basket/"
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    ITEMS_TO_BUY_NOW = (By.CSS_SELECTOR, ".basket-items")
	
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    SIGN_UP = (By.CSS_SELECTOR, "#login_form")
    SIGN_IN = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1")
    REG_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner>strong:nth-child(1)")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")