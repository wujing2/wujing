from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import unittest
import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains

class D90_match(unittest.TestCase):
    'D90选配'
    def setUp(self):
        self.dr=webdriver.Chrome()
        self.dr.get("https://mall.maxuscloud.com/p/pages/index.html")
        self.dr.maximize_window()
    def D90_match_Login(self):
        self.dr.find_element_by_xpath("/html/body/div[7]/div/div[1]/div/div[1]/a[1]").click()
        self.dr.implicitly_wait(10)
        self.dr.find_element_by_name("username").send_keys("17768609406")
        self.dr.find_element_by_name("password").send_keys("11111111")
        self.dr.add_cookie({'name':'Login_UserNumber', 'value':'username'})
        self.dr.add_cookie({'name':'Login_Passwd', 'value':'password'})
        self.dr.find_elements_by_class_name("form-control input-lg")
