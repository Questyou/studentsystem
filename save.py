def save(student):
    try:
        student_txt = open(filename , 'a')
    except Exception as e:
        student_txt = open(filename , 'w')
    for info in student:
        student_txt.write(str(info), "\n")
    student_txt.close()
