students = [{"name":"张三","score":95},
           {"name":"李四","score":80},
            {"name":"王五","score":60}]         
def show_names(students):
    for student in students:
        print(student["name"])
def show_scores(students):
    for student in students:
        print(f'{student["name"]} 的成绩是 {student["score"]}')          
def show_good_students(students):
    for student in students:
        if student["score"]   >= 90:
            print(student["name"])
show_names(students)
show_scores(students)
show_good_students(students)       