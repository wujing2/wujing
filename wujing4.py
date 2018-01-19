from selenium import webdriver
from time import sleep
import unittest
import HTMLTestRunner
import time

class testopen(unittest.TestCase):
    '网易邮箱登录'
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.get('http://mail.163.com/')
        self.dr.maximize_window()
    def test_wangye_login(self):
        self.dr.switch_to.frame('x-URS-iframe')
        self.dr.find_element_by_name("email").send_keys("17768609406")
        self.dr.find_element_by_name("password").send_keys("Wj07139865")
        self.dr.find_element_by_id("dologin").click()
        time.sleep(5)
        self.assertIn('网易邮',self.dr.title)

    def tearDown(self):
        self.dr.quit()
def suite():
    suiteTest=unittest.TestSuite()

    suiteTest.addTest(testopen("test_wangye_login"))
    return suiteTest
if __name__ == "__main__":
    filepath = 'D:\\wyresult.html'
    fp = open(filepath, 'wb')
    # 定义测试报告的标题与描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'我是测试报告的标题', description=u'我是测试报告的描述')
    runner.run(suite())
    fp.close()

