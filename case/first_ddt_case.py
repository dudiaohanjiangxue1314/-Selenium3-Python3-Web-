#coding=utf-8
import ddt
import sys
sys.path.append(r"D:\project_selenium3") #将工程路径加入到Python的搜索路径中
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner
import os
import time
from util.excel_util import ExcelUtil

ex = ExcelUtil()
data = ex.get_data()  #取出excel文件中的数据


@ddt.ddt
class FirstDataCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() #因为driver在其他函数中要使用，所以加上self使其变为全局的
        self.driver.get("http://www.5itest.cn/register")
        self.driver.maximize_window()  
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName #获取case的名字，用于后续的截图
                screenshot_name = case_name+'.png' #截图图片的名字
                dir_path = os.path.dirname(os.getcwd()) #获取上一级目录，即工程目录  
                file_path = os.path.join(dir_path,'report',screenshot_name) #截图保存路径
                self.driver.save_screenshot(file_path)
        self.driver.close()
    
    #邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
    '''
    @ddt.data(
            ['122','Mushishi11','111111',r'D:\selenium_image\test02.png','user_email_error','请输入有效的电子邮件地址'],
            ['@qq.com','Mushishi11','111111',r'D:\selenium_image\test02.png','user_email_error','请输入有效的电子邮件地址'],
            ['122@qq.com','Mushishi11','111111',r'D:\selenium_image\test02.png','user_email_error','请输入有效的电子邮件地址']
    )

    @ddt.unpack

    '''

    @ddt.data(*data)
    def test_register_case(self,data):
        email,username,password,file_name,assertCode,assertText = data        
        email_error = self.login.register_function(email,username,password,file_name,assertCode,assertText)
        self.assertFalse(email_error,'测试失败')



if __name__ == '__main__':
    dir_path = os.path.dirname(os.getcwd()) #获取上一级目录，即工程目录  
    file_path = os.path.join(dir_path,'report','first_ddt_case.html') #获取report文件夹下first_case.html目录路径
    f = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDataCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="this is second report",description="这是第二个报告",verbosity=2)
    runner.run(suite)
