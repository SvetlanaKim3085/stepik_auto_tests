
from .locators  import AddToBasket
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import CheckBasket
from .locators import ProductPageLocators
from .locators import BasePageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

class ProductPage(BasePage):        
    def add_to_basket(self):
        add_product= self.browser.find_element(*AddToBasket.Add_button)
        add_product.click()      
  
    def product_check(self):
        basket_product_name=self.browser.find_element(*CheckBasket.Product_name_basket)
        assert self.browser.find_element(*CheckBasket.PRODUCT).text== basket_product_name.text, f"Product name is not matched"

    def total_check(self):
        basket_total=self.browser.find_element(*CheckBasket.Total_basket)
        assert self.browser.find_element(*CheckBasket.PRICE).text == basket_total.text, f"Total is not matched"    

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    def should_disappeared_seccess_massage(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MASSAGE), \
        "Success message is disapeared, but should not be"