
from .pages.basket_page import BasketPage




def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link=link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.basket_empty()
    page.empty_basket_line()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page=BasketPage(browser,link)
    page.open()
    page.go_to_basket()
    page.basket_empty()
    page.empty_basket_line()