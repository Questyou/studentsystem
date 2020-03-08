import re
import os
import time

filename = "students.txt"  # 定义保存学生信息的文件名

def main():
    ctrl  = True
    while (ctrl):
        time.sleep(1)
        menu()
        option = input('请选择')
        #移除输入信息中非数字内容
        option_str = re.sub('\D', "" , option)
        if option_str in ['0','1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 0:
                print('您已退出学习信息管理系统')
                ctrl = False
            elif option_int == 1:
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


def menu():
    print('''
    =================学生信息管理系统===================
    ==                                                ==
    ==    -----------    功能菜单 ----------------    ==
    ==                                                ==
    ==     1. 录入学生信息                            ==
    ==     2. 查询学生信息                            ==
    ==     3. 删除学生信息                            ==
    ==     4. 修改学生信息                            ==
    ==     5. 学生信息排序                            ==
    ==     6. 统计学生总人数                          ==
    ==     7. 显示所有学生信息                        ==
    ==     0. 退出系统                                ==
    ====================================================
    ==说明：通过数字或者上下方向键选择菜单            ==
    ====================================================

    ''')

def save(student):
    try:
        student_txt = open(filename , 'a')
    except Exception as e:
        student_txt = open(filename , 'w')
    for info in student:
        student_txt.write(str(info) + "\n")
        #犯错误一次
    student_txt.close()

# def insert():
#     print('插入数据函数')
def insert ():
    stdentList =  []
    mark = True
    while mark:
        id = input('请输入ID（如1001）： ' )
        if not id :
            break
        name = input("请输入名字： ")
        if  not name:
            break
        try:
            english = int(input("请输入英语成绩："))
            python = int(input("请输入python成绩："))
            c = int(input("请输入c成绩："))
        except:
            print("输入无效，不是整型")
            continue
        student = {'id' : id , 'name' : name , 'english' : english,'python' : python ,  'c' : c}
        stdentList.append(student)
        inputMark = input("是否继续添加？ （y/n）")
        if inputMark  == "y":
            mark = True
        else:
            mark = False
        save(stdentList)
        print("学生录入完成！")

def delete():
    mark = True
    while mark:
        studentID = input("请输入要删除的学生ID")
        if studentID is not "":
            if os.path.exists(filename):
                with open(filename, 'r') as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = [ ]
            ifdel = False
            if student_old:
                with open(filename, 'w') as wfile:
                    d = {}
                    for list  in student_old:
                        d = dict(eval(list))
                        if d["id"] != studentID:
                            wfile.write(str(d) + '\n')
                        else:
                            ifdel = True
                    if ifdel:
                        print("ID 为 %s 的学生信息已经删除。。。。" % studentID)
                    else:
                        print("没有找到学生ID为  %s 的学生信息" % studentID)
            else:
                print('无学生信息')
                break
            show()
            inputMark = input("是否继续删除？   （y/n）:")
            if inputMark == "y":
                mark = True
            else:
                mark = False

    # print('')

def modify():
    show()
    if os.path.exists(filename):
        with   open(filename, 'r') as   rfile:
            student_old = rfile.readlines()
    else:
        return
    studentid = input('请输入要修改的学生ID: ')
    with open(filename , 'w') as wfile:
        for student in student_old:
            d = dict(eval(student))
            if d['id']  == studentid:
                print("找到这名学生信息，可以修改他的信息")
                while True:
                    try:
                        d['name'] = input('请输入姓名： ')
                        d['english'] = int(input('请输入英语成绩：'))
                        d['python'] = int(input('请输入python成绩'))
                        d['c'] = int(input('请输入c语音成绩'))
                    except:
                        print('输入信息有误，请重新输入')
                    else:
                        break
                student = str(d)
                wfile.write(student + "\n")
                print('修改成功')
            else:
                print('未找到该学员信息')
                wfile.write(student)
        mark = input('是否继续修改其他学生信息？ （y/n）:')
        if mark == 'y':
            modify()

# 下面是自己写的，后续根据自己的思路完善他
# def modify():
#     mark = True
#     while mark:
#         show()
#         studentID  = input('请输入要修改的学生ID')
#         if studentID :
#             if os.path.exists(filename):
#                 with open(filename, 'w') as rfile:
#                     student_old = rfile.readlines()
#             else:
#                 student_old = [ ]
#         ifmodify = False
#         if student_old:
#             with open(filename , 'w') as wfile:
#                 d = { }
#                 for list in student_old:
#                     d = dict(eval(list))
#                     if d['id']  == studentID:
#                         student_name = input("请输入学生姓名: ")
#
#                 save()
#         else:
#             print("无学生信息")
#                 # student_old = open(filename + '\n')
#     print('')

def show_student(studentList):
    if not studentList:
        print("无数据信息")
        return
    format_tittle = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_tittle.format('ID','名字','英语成绩','python成绩','C语言成绩','总成绩'))
    format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in studentList:
        print(format_data.format(info.get('id'), info.get('name') , str(info.get('english')) , str(info.get('python')) ,
                                 str(info.get('c')) ,  str(info.get('english') + info.get('python') + info.get('c')).center(12)))
    pass


def search():
    mark = True
    student_query = [ ]
    while mark:
        id = ' '
        name = ' '
        if os.path.exists(filename):
            # with open(filename, 'r') as rfile
            mode = input("按照ID查询请输入1，按照名称查询请输入2")
            if mode == '1':
                id = input('请输入学生ID： ')
            elif mode == "2":
                name = input("请输入学生名称： ")
            else:
                print('输入信息错误，请重新输入')
                search()
            with open(filename, 'r') as rfile:
                student = rfile.readlines()
                for list in student:
                    d = dict(eval(list))
                    if id  is not "":
                        if d['id']  == id:
                            student_query.append(d)
                    # 将elif改为了if name  否则进入不了判断
                    if name is not "":
                        if d['name'] == name:
                            student_query.append(d)
                show_student(student_query)
                student_query.clear()
                inputMark = input("是否继续查询？   （y/n）:")
                if inputMark == "y":
                    mark = True
                else:
                    mark = False
        else:
            print('暂未保存数据信息。。')
            return




    print('search')

def sort():
    show()
    if os.path.exists(filename):
        with   open(filename, 'r') as   rfile:
            student_old = rfile.readlines()
            student_new =  []
        for list in student_old:
            d = dict(eval(list))
            student_new.append(d)
    else:
        return
    ascORdesc = input("请选择：（0升序，1降序)：  ")
    if ascORdesc == '0':
        ascORdescBool = False
    elif ascORdesc == '1':
        ascORdescBool  = True
    else:
        print('输入信息有误，请重新输入')
        sort()
    mode = input('请选择排序方式（1、按照英语排序，2、按照python排序 3、按照c排序，0按照总成绩排序）')
    if mode == '1':
        student_new.sort(key=lambda x: x['english'] , reverse= ascORdescBool)
    elif mode == '2':
        student_new.sort(key=lambda x: x['python'], reverse=ascORdescBool)
    elif mode == '3':
        student_new.sort(key=lambda x: x['c'], reverse=ascORdescBool)
    elif mode == '0':
        student_new.sort(key=lambda x: x['english'] + x['python'] + x['c'], reverse=ascORdescBool)
    else:
        print("输入数据有误，请重新输入")
        sort()
    show_student(student_new)

def total():
    if os.path.exists(filename):
        with open(filename,'r') as rfile:
            student_old = rfile.readlines()
            # lenth = len(student_old)
            # print(lenth)
            if student_old:
                print("一共有 %d 名学生" % len(student_old))
                # print('stop')
            else:
                print('没有学生信息')
    else:
        print('暂未保存数据信息.....')

def show():
    student_new = [ ]
    if os.path.exists(filename):
        with    open(filename, 'r') as  rfile:
            student_info =rfile.readlines()
            # print(student_info)
        for list in student_info:
            student_new.append(eval(list))
        if student_new:
            show_student(student_new)
            # print(str(student_new) + '\n')
            print('')
    else:
        print("暂未保存数据信息")





main()
