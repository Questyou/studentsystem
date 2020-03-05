from save import save
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
        if inputMark  == y :
            mark = True
        else:
            mark = False

        save(stdentList)
        print("学生录入完成！")

