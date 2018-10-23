#coding=utf-8
import sys
sys.path.append(r"D:\project_selenium3") #将工程路径加入到Python的搜索路径中
from selenium import webdriver
from base.find_element import FindElement
import time

#关键字驱动方法类
class ActionMethod(object):
    
    #打开浏览器
    def open_browser(self,browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
        
    
    #输入地址
    def get_url(self,url):
        self.driver.get(url)
    
    #定位元素
    def get_element(self,key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element
    
    #输入元素
    def element_send_keys(self,value,key):
        element = self.get_element(key)
        element.send_keys(value)

    #点击元素
    def click_element(self,key):
        self.get_element(key).click()
    
    #等待
    def sleep_time(self):
        time.sleep(3)
    
    #获取title
    def get_title(self):
        title = self.driver.title
        return title
    
    #关闭浏览器
    def close_browser(self):
        self.driver.close()
            
    