import re
# import sys
# sys.path.append('D:\PyCharmObJect\studentsystem')
from main import *


def main():
    ctrl  = True
    while (ctrl):
        # from studentsystem.main import menu
        menu()
        option = input('请选择')
        #移除输入信息中非数字内容
        option_str = re.sub('\D', "" , option)
        if option_str in ['0','1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 0:
                print('您已退出学习信息管理系统')
                ctrl = False
            elif option_int == 1 :
                insert()
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                total()
            elif option_int == 7:
                show()
            else:
                print('输入错误，请重新输入')


def delete():
    print('')

def modify():
    print('')

def sort():
    print('')

def total():
    print('')

def show():
    print('')

def insert():
    print('插入数据函数')

def search():
    print('search')

main()
