#coding=utf-8
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import time

class GetCode(object):
    def __init__(self,driver):
        self.driver = driver
    
    #获取验证码图片
    def get_code_image(self,file_name):
        '''
        思想：先保存整个网页，然后从中裁剪出验证码图片
        '''
        self.driver.save_screenshot(file_name) #保存整个页面为图片格式
        code_element = self.driver.find_element_by_id("getcode_num") #定位到验证码图片
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top

        im = Image.open(file_name) #使用pillow中的Image方法打开之前保存的图片
        img = im.crop((left,top,right,height)) #使用crop方法进行裁剪，取出图片中的验证码图片
        img.save(file_name) #保存裁剪出的验证码图片
        time.sleep(1)

    #解析图片获取验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name) #文件上传时设置
        res = r.post()
        time.sleep(1)
        text = res.json()['showapi_res_body']
        code = text['Result']
        return code
        