from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_to_exist_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY_NOW), "There are items in the basket, but should not be"
		   
    def should_be_basket_empty_text(self):
        assert not self.is_not_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), "Basket is not empty"

    def should_be_basket_url(self):
	    assert BasketPageLocators.BASKET_URL in self.browser.current_url, "Login url is not correct"
        # реализуйте проверку на корректный url адрес