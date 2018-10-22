#coding=utf-8
import xlrd

class ExcelUtil(object):

    def __init__(self,excel_path=None,index=None):   #index值excel文件中的sheet
        if excel_path == None:
            excel_path = "D:\project_selenium3\config\casedata.xlsx"
        
        if index == None:
            index = 0
        
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]
        self.rows = self.table.nrows #获取行数
    
    def get_data(self):
        result = []
        for i in range(self.rows):
            col = self.table.row_values(i)
            result.append(col)
        return result


if __name__ == '__main__':
    ex = ExcelUtil()
    print(ex.get_data())



