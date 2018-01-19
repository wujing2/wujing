from selenium import webdriver

from time import sleep
import unittest
import HTMLTestRunner
from selenium.webdriver.common.action_chains import  ActionChains
import time
import gettext

class D90_open(unittest.TestCase):
    'D90选配后台登录'
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.get('http://10.135.78.4:8080/adminLogin.jsp')
        self.dr.maximize_window()
    def D90_background_login(self):
        self.dr.find_element_by_name("loginUser").send_keys("1")
        self.dr.find_element_by_name("password").send_keys("1")
        self.dr.find_element_by_id("btnLogin").click()
        time.sleep(5)
        self.assertIn('D90',self.dr.title)
        self.dr.find_element_by_xpath('//*[@id="menu1"]/a/em').click()
        char_text =self.dr.find_element_by_xpath('//*[@id="yui-main"]/div/div[1]/div/div[1]/h3').text
        self.assertEqual(char_text,'车型查询')

    def tearDown(self):
        pass
def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(D90_open('D90_background_login'))
    return suiteTest
if __name__ == "__main__":
    filepath = 'D:\\csbg.html'
    fp = open(filepath, 'wb')
    # 定义测试报告的标题与描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告标题', description=u'测试报告描述')
    runner.run(suite())
    fp.close()