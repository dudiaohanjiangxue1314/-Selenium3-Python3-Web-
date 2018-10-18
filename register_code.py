#coding=utf-8
from selenium import webdriver
from PIL import Image
import random
from ShowapiRequest import ShowapiRequest
import time
driver = webdriver.Chrome()

#浏览器初始化
def driver_init():
    driver.get("http://www.5itest.cn/register") #打开页面
    driver.maximize_window() #窗口最大化
    time.sleep(5)

#获取element信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

#获取随机数
def get_range_user():
    user_info = ''.join(random.sample('1234567890abcdefghijklmn',8))
    return user_info

#获取验证码图片
def get_code_image(file_name):
    '''
    思想：先保存整个网页，然后从中裁剪出验证码图片
    '''
    driver.save_screenshot(file_name) #保存整个页面为图片格式
    code_element = driver.find_element_by_id("getcode_num") #定位到验证码图片
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width']+left
    height = code_element.size['height']+top

    im = Image.open(file_name) #使用pillow中的Image方法打开之前保存的图片
    img = im.crop((left,top,right,height)) #使用crop方法进行裁剪，取出图片中的验证码图片
    img.save(file_name) #保存裁剪出的验证码图片

#解析图片获取验证码
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addFilePara("image", file_name) #文件上传时设置
    res = r.post()
    text = res.json()['showapi_res_body']['Result']
    return text

#运行主程序
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info + '@126.com'
    file_name = r"D:\selenium_image\test01.png"
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys(111111)
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("captcha_code").send_keys(text)
    get_element("register-btn").click()
    driver.close() #关闭driver，一定要有，否则电脑速度会越来越慢

run_main()
