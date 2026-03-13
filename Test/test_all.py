import pytest
import json
from Case_Study_2_Project.Pages.RegisterPage import RegisterPage
from Case_Study_2_Project.Pages.LoginPage import LoginPage
from Case_Study_2_Project.Pages.AddToCartPage import AddToCartPage
import allure
from allure_commons.types import AttachmentType

def data_setup():
    with open(r"C:\Users\Harsh Upadhyay\OneDrive\Desktop\Repos\Case_Study_2_Project\Data\data.json","r") as file:
        data = json.load(file)
        return [data]

@pytest.mark.parametrize("testdata",data_setup())
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.register
@pytest.mark.order(1)
def test_registration(test_setup,testdata):
    driver=test_setup
    registration_data = testdata['registration_data']

    firstname = registration_data['firstname']
    lastname = registration_data['lastname']
    email = registration_data['email']
    password = registration_data['password']
    register_page = RegisterPage(driver)
    register_page.click_register_button()
    register_page.select_gender()
    register_page.enter_first_name(firstname)
    register_page.enter_last_name(lastname)
    register_page.enter_email(email)
    register_page.enter_password(password)
    register_page.enter_confirmpassword(password)
    register_page.complete_registration()
    register_page.confirm_registration()
    allure.attach(driver.get_screenshot_as_png(),name="Registration",attachment_type=AttachmentType.PNG)
    register_page.click_continue_button()
    register_page.click_logout()

@pytest.mark.parametrize("testdata",data_setup())
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.login
@pytest.mark.order(2)
def test_login(test_setup,testdata):
    driver=test_setup
    login_data = testdata['login_data']
    email=login_data['email']
    password=login_data['password']
    login_page = LoginPage(driver)
    login_page.click_login_link()
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login_button()

@pytest.mark.regression
@pytest.mark.cart
@pytest.mark.order(3)
def test_add_to_cart(test_setup):
    driver=test_setup
    add_to_cart_page = AddToCartPage(driver)
    add_to_cart_page.move_mouse_to_computer_menu()
    add_to_cart_page.click_desktop_menu()
    add_to_cart_page.add_simple_computer_to_cart()
    add_to_cart_page.select_processor()
    add_to_cart_page.click_add_to_cart()
    add_to_cart_page.open_shopping_cart()