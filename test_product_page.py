from .pages.product_page import PageObject
from .pages.basket_page import BasketPage
import pytest, time

@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                 8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    browser.delete_all_cookies()
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.should_be_add_button()
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message_about_adding()
    product_page.should_be_message_basket_total()

@pytest.mark.skip(reason="delete this mark for test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    #browser.delete_all_cookies()
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.should_not_be_success_message()

@pytest.mark.skip(reason="delete this mark for test")
def test_guest_cant_see_success_message(browser): 
    #browser.delete_all_cookies()
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()
	
@pytest.mark.skip(reason="delete this mark for test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    #browser.delete_all_cookies()
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.should_not_be_dissapper_message()

@pytest.mark.skip(reason="delete this mark for test")
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = PageObject(browser, link)
    product_page.open()
    #product_page.go_to_login_page()
    product_page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.should_be_cart_link()
    product_page.go_to_cart()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_not_to_exist_items_in_the_basket()
    basket_page.should_be_basket_empty_text()