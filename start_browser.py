#coding=utf-8
from selenium import webdriver
import random
import time
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get("http://www.5itest.cn/register?goto=/")
time.sleep(5)

driver.save_screenshot(r"D:\selenium_image\imooc.png") #保存整个页面为图片格式
code_element = driver.find_element_by_id("getcode_num") #定位到验证码图片
print(code_element.location) #输出格式为{'x': 550, 'y': 527}的值
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top

im = Image.open(r"D:\selenium_image\imooc.png") #使用pillow中的Image方法打开之前保存的图片
img = im.crop((left,top,right,height)) #使用crop方法进行裁剪，取出图片中的验证码图片
img.save(r"D:\selenium_image\imooc1.png") #保存裁剪出的验证码图片

driver.close()



# emial_element = driver.find_element_by_id("register_email")
# for i in range(5):
#     user_email = ''.join(random.sample('123456789abcdef',6))+'@126.com'
#     print(user_email)



# print(emial_element.get_attribute("placeholder"))
# emial_element.send_keys("andy@126.com")
# print(emial_element.get_attribute("value"))
# driver.find_element_by_xpath("//*[@id='register_nickname']").send_keys("xiaoming")
# print(EC.title_contains("注册"))

