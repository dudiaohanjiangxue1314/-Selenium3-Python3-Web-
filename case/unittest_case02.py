#coding=utf-8
import unittest

class FirstCase02(unittest.TestCase):
    
    '''
    @classmethod是装饰器，setupClass是unittest提供的所有case执行的前置条件
    '''
    @classmethod
    def setUpClass(cls):
        print("这是所有case执行的前置条件")


    @classmethod
    def tearDownClass(cls):
        print("这是所有case执行的后置条件")

    def setUp(self):
        print("前置条件")
    
    def tearDown(self):
        print("后置条件")  

    def test_001(self):
        print("这是第001个case")
    
    @unittest.skip("不执行第2条case")
    def test_002(self):
        print("这是第002个case")
    

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite() #创建一个测试套
    suite.addTest(FirstCase('test_002'))  #将要执行的case名加入到测试套中
    suite.addTest(FirstCase('test_001'))
    unittest.TextTestRunner().run(suite) #运行测试套

