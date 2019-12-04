from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    Login_Form=(By.CSS_SELECTOR, "#login_form")
    Registration_Form=(By.CSS_SELECTOR, "#register_form")

class AddToBasket():
    Add_button=(By.CSS_SELECTOR, "#add_to_basket_form > button")

class CheckBasket():
    Product_name_basket=(By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    Total_basket=(By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRODUCT=(By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRICE=(By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")

class ProductPageLocators():
    SUCCESS_MESSAGE= (By.CSS_SELECTOR, "#messages > div:nth-child(1)")