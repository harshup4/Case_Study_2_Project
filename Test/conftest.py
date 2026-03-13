import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def test_setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    s=Service("C:\\Users\\Harsh Upadhyay\\OneDrive\\Desktop\\Repos\\test-repo1\\chromium\\chromedriver.exe")
    driver = webdriver.Chrome(options=options,service=s)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    yield driver