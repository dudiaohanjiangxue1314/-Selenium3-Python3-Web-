#coding=utf-8
from page.register_page import RegisterPage
from util.get_code import GetCode


class RegisterHandle(object):
    def __init__(self,driver):
        self.driver = driver
        self.register_p = RegisterPage(self.driver)
    #输入邮箱
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)
        
    #输入用户名
    def send_user_name(self,username):
        self.register_p.get_username_element().send_keys(username)

    #输入密码
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)

    #输入验证码
    def send_user_code(self,file_name):
        get_code_text = GetCode(self.driver)
        code = get_code_text.code_online(file_name)
        self.register_p.get_code_element().send_keys(code)


    #获取文字信息
    def get_user_text(self,info,user_info):
        try:
            if info == 'user_email_error':
                text = self.register_p.get_email_error_element().text
            elif info == 'user_name_error':
                text = self.register_p.get_name_error_element().text
            elif info == 'password_error':
                text = self.register_p.get_password_error_element().text
            else:
                text =self.register_p.get_code_error_element().text
        except:
            text = None
        return text



    #点击注册按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()

    #获取注册按钮文字
    def get_register_text(self):
        return self.register_p.get_button_element().text



if __name__ == '__main__':
    # driver = webdriver.Chrome()
    # driver.get("http://www.5itest.cn/register") #打开页面
    # driver.maximize_window() #窗口最大化
    # time.sleep(5)
    # file_name = r"D:\selenium_image\test01.png"
    # register_handle = RegisterHandle(driver)
    # register_handle.send_user_email("haha@126.com")
    # register_handle.send_user_name("xiaoli")
    # register_handle.send_user_password("111111")
    # register_handle.send_user_code(file_name)
    # print(register_handle.get_user_text("user_email_error","user_email_error"))
    # print(register_handle.get_user_text("user_name_error","user_name_error"))
    # print(register_handle.get_user_text("password_error","password_error"))
    # print(register_handle.get_user_text("code_text_errorr","code_text_errorr"))

    # register_handle.click_register_button()
    # time.sleep(10)
    # driver.close()
