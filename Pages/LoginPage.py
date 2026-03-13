from .BasePage import BasePage

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    login_link = ("link text","Log in")
    email = ("id","Email")
    password = ("id","Password")
    login_button = ("xpath","//input[@value='Log in']")

    def click_login_link(self):
        self.click_element(self.login_link)
    def enter_email(self,text):
        self.input_text(self.email,text)
    def enter_password(self,text):
        self.input_text(self.password,text)
    def click_login_button(self):
        self.click_element(self.login_button)
