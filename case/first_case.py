#coding=utf-8
import sys
sys.path.append(r"D:\project_selenium3") #将工程路径加入到Python的搜索路径中
from business.register_business import RegisterBusiness
from selenium import webdriver


class FirstCase(object):
    def __init__(self):
        driver = webdriver.Chrome()
        driver.get("http://www.5itest.cn/register")
        driver.maximize_window()
       
        self.login = RegisterBusiness(driver)

    def test_login_email_error(self):
        email_error = self.login.login_email_error('34','user111','111111','test1')
        if email_error == True:
            print("注册成功了，此条case执行失败")


    
    def test_login_username_error(self):
        username_error = self.login.login_name_error('34','user111','111111','test1')
        if username_error == True:
            print("注册成功了，此条case执行失败")

    def test_login_password_error(self):
        password_error = self.login.login_password_error('34','user111','111111','test1')
        if password_error == True:
            print("注册成功了，此条case执行失败")

    def test_login_code_error(self):
        code_error = self.login.login_code_error('34','user111','111111','test1')
        if code_error == True:
            print("注册成功了，此条case执行失败")

    def test_login_success(self):
        success = self.login.user_base("111@qq.com","ss222","111111")
        if self.login.register_succes() == True:
            print('注册成功')

        
            

