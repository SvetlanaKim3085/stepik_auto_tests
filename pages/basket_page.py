from .base_page import BasePage
from .locators import  CheckBasket
from .locators import BasketLink



class BasketPage(BasePage):
    def basket_empty(self):
        assert self.is_not_element_present(*CheckBasket.PRODUCT), "Basket is  empty, but should not be"

    def empty_basket_line(self):
        assert self.is_element_present(*BasketLink.BASKET_EMPTY_LINE), "Basket is not empty"
        


