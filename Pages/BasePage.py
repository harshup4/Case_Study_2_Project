from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.exp_wait = WebDriverWait(self.driver,10)
        self.action = ActionChains(self.driver)
    def wait_for_element(self,locator):
        return self.exp_wait.until(ec.visibility_of_element_located(locator))
    
    def wait_for_element_to_be_clickable(self,locator):
        return self.exp_wait.until(ec.element_to_be_clickable(locator))
    def input_text(self,locator,text):
        element = self.wait_for_element(locator)
        element.send_keys(text)
    def click_element(self,locator):
        element = self.wait_for_element_to_be_clickable(locator)
        element.click()
    def get_text(self,locator):
        element = self.wait_for_element(locator)
        return element.text
    def mouseover_element(self,locator):
        element=self.wait_for_element(locator)
        self.action.move_to_element(element).perform()
    def scroll_to_element(self,locator):
        element=self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    