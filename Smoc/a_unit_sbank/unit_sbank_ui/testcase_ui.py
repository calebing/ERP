# import sys
# sys.path.append("D:/Samyang")
import time
import unittest
from E_business import operation
import os.path
from selenium import webdriver
class TestCase(unittest.TestCase,operation):
    Mom_assert = os.path.join(os.path.dirname(__file__) + '/Data/Mom_assert.yml')
    Mom_element = os.path.join(os.path.dirname(__file__) + '/Data/Mom_element.yml')
    Mom_variable = os.path.join(os.path.dirname(__file__) + '/Data/Mom_variable.yml')
    def setUp(self):
        self.driver=webdriver.Chrome('C:/chrom/Chrome/Application/chromedriver.exe')
        self.driver.maximize_window()
        self.login()
    def tearDown(self):
        self.driver.quit()


    def test001(self):
        '''
        分仓设置-删除一部分仓库性质用例关联
        :return:
        '''
        self.click('setting')

if __name__ == '__main__':
    unittest.main()
