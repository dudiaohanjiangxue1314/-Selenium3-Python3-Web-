#coding=utf-8
import unittest
import os

class RunCase(unittest.TestCase):
    def test_case01(self):
        case_path = os.getcwd()
        suite = unittest.defaultTestLoader.discover(case_path,'unittest_*.py')
        unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    unittest.main()
    