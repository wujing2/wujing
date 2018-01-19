import unittest
import HTMLTestRunner
class testadd(unittest.TestCase):
    def setUp(self):
        pass
    def test_add1(self):
        self.assertEqual(3+5,8)
    def test_add2(self):
        self.assertEqual(0+8+7,15)
    def tearDown(self):
        pass
def suite():
    suiteTest=unittest.TestSuite()
    suiteTest.addTest(testadd("test_add1"))
    suiteTest.addTest(testadd("test_add2"))
    return suiteTest
if __name__ == "__main__":
    filepath = 'D:\\pyresult.html'
    fp = open(filepath, 'wb')
    # 定义测试报告的标题与描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'我是测试报告的标题',description=u'我是测试报告的描述')
    runner.run(suite())
    fp.close()