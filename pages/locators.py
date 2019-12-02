from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    Login_Form=(By.CSS_SELECTOR, "#login_form")
    Registration_Form=(By.CSS_SELECTOR, "#register_form")


