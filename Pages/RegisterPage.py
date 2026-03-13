from .BasePage import BasePage

class RegisterPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    register_button = ("partial link text","Register")
    gender = ("id","gender-male")
    firstname = ("id","FirstName")
    lastname = ("id","LastName")
    email = ("id","Email")
    password = ("id","Password")
    confirmpassword = ("id","ConfirmPassword")
    complete_register_button = ("id","register-button")
    registration_successfull_text = ("xpath","//div[@class='result']")
    continue_button = ("xpath","//input[@value='Continue']")
    log_out_button = ("link text","Log out")



    def click_register_button(self):
        self.click_element(self.register_button)
    
    def select_gender(self):
        self.click_element(self.gender)
    
    def enter_first_name(self,text):
        self.input_text(self.firstname,text)
    def enter_last_name(self,text):
        self.input_text(self.lastname,text)
    def enter_email(self,text):
        self.input_text(self.email,text)
    def enter_password(self,text):
        self.input_text(self.password,text)
    def enter_confirmpassword(self,text):
        self.input_text(self.confirmpassword,text)
    def complete_registration(self):
        self.click_element(self.complete_register_button)
    def confirm_registration(self):
        assert "completed" in self.get_text(self.registration_successfull_text)
    def click_continue_button(self):
        self.click_element(self.continue_button)
    def click_logout(self):
        self.click_element(self.log_out_button)
