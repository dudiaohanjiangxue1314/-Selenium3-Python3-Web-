#coding=utf-8
import unittest

class FirstCase01(unittest.TestCase):
    
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

    def test_01(self):
        print("这是第01个case")
    
    @unittest.skip("不执行第2条case")
    def test_02(self):
        print("这是第02个case")
    

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite() #创建一个测试套
    suite.addTest(FirstCase('test_02'))  #将要执行的case名加入到测试套中
    suite.addTest(FirstCase('test_01'))
    unittest.TextTestRunner().run(suite) #运行测试套

