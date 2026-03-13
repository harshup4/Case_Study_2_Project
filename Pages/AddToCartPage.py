from .BasePage import BasePage

class AddToCartPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    computer_menu = ("xpath","(//a[contains(text(),'Computers')])[1]")
    desktop_menu = ("xpath","(//a[contains(text(),'Desktop')])[1]")
    simple_computer_label = ("link text","Simple Computer")
    add_to_cart_button_one = ("xpath","//a[text()='Simple Computer']/../..//input[@value='Add to cart']")
    slow_radio = ("xpath","//label[contains(text(),'Processor')]/following::input[1]")
    add_to_cart_button_two = ("css selector","input#add-to-cart-button-75")
    shopping_cart_link = ("xpath","//span[text()='Shopping cart']")
    close_button = ("xpath","//span[@title='Close']")
    go_to_cart_button = ("xpath","//input[@value='Go to cart']")

    def move_mouse_to_computer_menu(self):
        self.mouseover_element(self.computer_menu)
    def click_desktop_menu(self):
        self.click_element(self.desktop_menu)
    def add_simple_computer_to_cart(self):
        self.scroll_to_element(self.simple_computer_label)
        self.click_element(self.add_to_cart_button_one)
    def select_processor(self):
        self.click_element(self.slow_radio)
    def click_add_to_cart(self):
        self.scroll_to_element(self.add_to_cart_button_two)
        self.click_element(self.add_to_cart_button_two)
    def open_shopping_cart(self):
        self.click_element(self.close_button)
        self.scroll_to_element(self.shopping_cart_link)
        self.mouseover_element(self.shopping_cart_link)
        self.click_element(self.go_to_cart_button)

    

        
