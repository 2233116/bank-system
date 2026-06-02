z = []
def add_student():
        a = input("请输入姓名")
        if a == "":
           print("姓名不能空")
        elif a in z:
           print("该学生已存在")
        else:
           z.append(a)
           print("添加成功")
def remove_student():
       c = input("请输入删除学生的姓名")
       if c in z:
           z.remove(c)
def show_student():
       for d in z :
          print(d)        
while True:
    b = (input("请输入操作：\n1.添加学生\n2.删除学生\n3.查看学生\n4.退出"))
    if b ==  "1": 
         add_student()
    elif b == "2":
         remove_student()
    elif b == "3":
         show_student()
    elif b == "4":
       print("退出")
       break 
              
