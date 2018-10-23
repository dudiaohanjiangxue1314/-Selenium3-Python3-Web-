#coding=utf-8
import xlrd
from xlutils.copy import copy
import time

class ExcelUtil(object):

    def __init__(self,excel_path=None,index=None):   #index值excel文件中的sheet
        if excel_path == None:
            self.excel_path = "D:\project_selenium3\config\casedata.xls"
        else:
            self.excel_path = excel_path
        
        if index == None:
            index = 0
        
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]
    
    #获取excel行数
    def get_lines(self):
        rows = self.table.nrows #获取行数
        if rows>=1:
            return rows
        return None

    #获取excel的数据，按照每行一个list，添加到一个大的list里面，形如 #[[],[]]
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows !=None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None


    #获取单元格的数据
    def get_col_value(self,row,col):
        if self.get_lines()>row:
            data = self.table.cell(row,col).value 
            return data
        return None

    #写入数据
    def write_value(self,row,col,value):
        read_value =  xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row,col,value)
        write_data.save(self.excel_path)  #注意xlutils的save方法只能保存为xls格式的文件，所有在设置保存路径的时候一定要修改为xls才行
        time.sleep(1) #让系统有足够的时间来保存文件



if __name__ == '__main__':
    ex = ExcelUtil("D:\project_selenium3\config\keyword.xls")
    print(ex.write_value(2,7,'haha'))



