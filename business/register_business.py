#coding=utf-8
from handle.register_handle import RegisterHandle

class RegisterBusiness(object):
    def __init__(self,driver):
        self.driver = driver
        self.register_h = RegisterHandle(self.driver)
    
    def user_base(self,email,name,password,file_name):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(file_name)
        self.register_h.click_register_button()
    
    #注册成功
    def register_succes(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_register_text() == None:
            return True
        else:
            return False
    
    #邮箱错误
    def login_email_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text("email_error","请输入有效的电子邮件地址") == None:
            return True
        else:
            return False
    

    #用户名错误
    def login_name_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text("user_name_error","字符长度必须大于等于4，一个中文字算2个字符") == None:
            return True
        else:
            return False

    #密码错误
    def login_password_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text("password_error","最少需要输入 5 个字符") == None:
            return True
        else:
            return False

    #验证码错误
    def login_code_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text("code_text_error","验证码错误") == None:
            return True
        else:
            return False

    #注册功能整合，是对上面几个方法的封装，以后只需要调用这一个方法即可
    def register_function(self,email,username,password,file_name,assertCode,assertText):
        self.user_base(email,username,password,file_name)
        if self.register_h.get_user_text(assertCode,assertText) == None:
            return True
        else:
            return False

