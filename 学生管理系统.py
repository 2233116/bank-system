students = [{"name":"张三","age":18},{"name":"李四","age":19},{"name":"王五","age":20}]
def add_student():
        name = input("姓名")
        age = input("年龄")
        if name == "":
               print("姓名不能空")        
        for name in students:
               print("该学生已存在")
               break        
        else:  
            students.append({"name":name,"age":age})
            print("添加成功")
def remove_student():
       name = input("请输入删除学生的姓名")
       for c in students:
         if name in students:
           students.remove(c)
           print("删除成功")
           break
         else:
            print("该学生不存在")
def show_student():
         for d in students :
            print(f'姓名：{d["name"]}\n年龄:{d["age"]}') 
def find_student():
     name = input("请输入姓名")
     for e in students:     
         if name in students:
            print(f'姓名:{e["name"]}\n年龄:{e["age"]}')
                                
while True:
    b = (input("请输入操作：\n1.添加学生\n2.删除学生\n3.查看学生\n4.查找学生\n5.退出"))
    if b ==  "1": 
         add_student()
    elif b == "2":
         remove_student()
    elif b == "3":          
            show_student()
    elif b == "4":
            find_student()
    elif b == "5":
       print("退出")
       break 
              
