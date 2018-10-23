#coding=utf-8
import sys
sys.path.append(r"D:\project_selenium3") #将工程路径加入到Python的搜索路径中
from util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod

class KewordCase(object):
    def run_main(self):
        self.action_method = ActionMethod() 
        handle_excel = ExcelUtil("D:\project_selenium3\config\keyword.xls")
        case_lines = handle_excel.get_lines() #获取case表格中的行数
        if case_lines:
            for i in range(1,case_lines): #跳过case表格中的第一行内容
                is_run = handle_excel.get_col_value(i,3) #获取是否执行列的值
                if is_run == 'yes':   #根据执行列是否为yes，如果是yes，则执行相应的case
                    except_result_method = handle_excel.get_col_value(i,7) #预期结果方法值
                    except_result = handle_excel.get_col_value(i,8) #预期结果
                    method = handle_excel.get_col_value(i,4) #获取执行方法
                    send_value = handle_excel.get_col_value(i,5) #获取需要输入的数据
                    handle_value = handle_excel.get_col_value(i,6) #获取操作元素
                    self.run_method(method,send_value,handle_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result) #获取预期结果值
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i,9,'pass')
                            else:
                                handle_excel.write_value(i,9,'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method,except_value[1])
                            if result:
                                handle_excel.write_value(i,9,'pass')
                            else:
                                handle_excel.write_value(i,9,'fail')
                        else:
                            print("没有else")
                    else:
                        print("预期结果为空")

                            

    #获取预期结果值
    def get_except_result_value(self,data):
        return data.split('=')


    '''
    @method:执行方法
    @send_value:输入的数据
    @handle_value:操作元素
    '''
    def run_method(self,method,send_value='',handle_value=''):
        method_value = getattr(self.action_method,method) #此处利用python的反射机制来实现由字符串来调用相应的方法
        if send_value =='' and  handle_value !='':
            result = method_value(handle_value)
        elif send_value == '' and handle_value == '':
            result = method_value()
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        else:
            result = method_value(send_value,handle_value)
        return result




if __name__ == '__main__':
    test = KewordCase()
    test.run_main()

