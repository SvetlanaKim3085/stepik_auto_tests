from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import Registration


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

  

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.Login_Form), "Login form  is not presented"    
       

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.Registration_Form), "Registration form  is not presented"
    
    def register_new_user(self,email,password):
        email_element=self.browser.find_element(*Registration.email)
        email_element.send_keys(email)
        password_element=self.browser.find_element(*Registration.password)
        password_element.send_keys(password)
        CONFIRM_PASSWORD=self.browser.find_element(*Registration.confirm_password)
        CONFIRM_PASSWORD.send_keys(password)
        REGISTR_BUTTON=self.browser.find_element(*Registration.registr_button)
        REGISTR_BUTTON.click()

    def user_is_logined(self):
        assert self.is_element_present(*Registration.account), "User is not logined"
        
        
        
        
        
        
        
      