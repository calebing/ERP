import time
from selenium import webdriver
from Method_ui  import BasePage
from selenium.webdriver.common.by import By
import os.path

class operation(BasePage):
    Mom_assert = os.path.join(os.path.dirname(__file__) + '/Data/Mom_assert.yml')
    Mom_element = os.path.join(os.path.dirname(__file__) + '/Data/Mom_element.yml')
    Mom_variable = os.path.join(os.path.dirname(__file__) + '/Data/Mom_variable.yml')
    def login(self):
        self.g_url('url65')
        self.input('long_username','user')
        self.input('long_password','password')
        self.click('long_button')







if __name__ == '__main__':

    driver = webdriver.Chrome('F:/chrom/Chrome/Application/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.find_element_by_class_name('aaa')
    driver.maximize_window()
    a=operation(driver)
