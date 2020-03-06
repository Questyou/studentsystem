import re
import os
# import sys
# sys.path.append('D:\PyCharmObJect\studentsystem')


filename = "students.txt"  # 定义保存学生信息的文件名

def main():
    ctrl  = True
    while (ctrl):
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
                        print("没有占到学生ID为  %s 的学生信息" % studentID)
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
    print('')

def sort():
    print('')

def total():
    print('')

def show():
    student_new = [ ]
    if os.path.exists(filename):
        with    open(filename, 'r') as  rfile:
            student_info =rfile.readlines()
            print(student_info)
        for list in student_info:
            student_new.append(eval(list))
        if student_new:
            # show_student(student_new)
            print('')
    else:
        print("暂未保存数据信息")



def search():
    print('search')

main()
