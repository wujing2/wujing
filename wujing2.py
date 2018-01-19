import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('FOO'.upper(),'FOO')

    def test_isupper(self):
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        mystr = 'Hello World'
        self.assertEqual(mystr.split(),['Hello','World'])

if __name__ =='__main__':
    # unittest.main  为测试提供了入口
    unittest.main()