from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

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

class BasketLink():
    VIEW_BASKET=(By.CSS_SELECTOR,"#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    BASKET_EMPTY_LINE=(By.CSS_SELECTOR, "#content_inner > p") 

class Registration():
    email=(By.CSS_SELECTOR,"#id_registration-email")
    password=(By.CSS_SELECTOR, "#id_registration-password1")
    confirm_password=(By.CSS_SELECTOR, "#id_registration-password2")
    registr_button=(By.CSS_SELECTOR, "#register_form > button")
    account=(By.CSS_SELECTOR, "#top_page > div.navbar-collapse.account-collapse.collapse > div > ul > li:nth-child(1) > a")