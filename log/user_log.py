#coding=utf-8
import logging
import os
import datetime

class UserLog(object):
    
    def __init__(self):
        self.logger = logging.getLogger(__name__) #创建一个Logger对象
        # 以下三行为清空上次文件,详细介绍见：https://blog.csdn.net/Chelydra/article/details/79850366
        #https://www.jb51.net/article/64746.htm
        # 这为清空当前文件的logging 因为logging会包含所有的文件的logging
        logging.Logger.manager.loggerDict.pop(__name__)
        # 将当前文件的handlers 清空
        self.logger.handlers = []
        # 然后再次移除当前文件logging配置
        self.logger.removeHandler(self.logger.handlers)
        # 这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG) #设置等级

            #文件输出名字和路径
            base_dir = os.path.dirname(os.path.abspath(__file__)) #获取当前文件路径的上一层路径，abspath方法是获得绝对路径
            log_dir = os.path.join(base_dir,"logs") #获得logs文件夹的路径
            log_name = datetime.datetime.now().strftime("%Y-%m-%d")+".log" #以当前时间来命名当前log日志的名字
            log_file_path = os.path.join(log_dir,log_name) #获得整个log日志的完整路径        

            #控制台输出
            #consle = logging.StreamHandler() #创建处理流
            #logger.addHandler(consle) #将流加入到Logger中
            #文件输出日志
            self.file_handle = logging.FileHandler(log_file_path,'a',encoding='utf-8') 
            self.file_handle.setLevel(logging.INFO) #设置handle处理的级别
            formatter = logging.Formatter("%(asctime)s %(filename)s-->%(funcName)s %(lineno)d %(levelname)s---->%(message)s") #格式
            self.file_handle.setFormatter(formatter)
            self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger

    def close_handle(self):      
        self.logger.removeHandler(self.file_handle) #移除handler
        self.file_handle.close()


if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.info("test")
    user.close_handle()