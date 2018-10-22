#coding=utf-8
import ddt
import unittest

@ddt.ddt
class DataTest(unittest.TestCase):
    

    def setUp(self):
        print("这是个setUp")

    def tearDown(self):
        print("这是个tearDown")

    @ddt.data(
        [1,2],
        [3,4],
        [5,6]
    )

    @ddt.unpack
    def test_add(self,a,b):
        print(a+b)
    

if __name__ == '__main__':
    unittest.main()
    
