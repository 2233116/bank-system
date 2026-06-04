file = open("students.txt","r",encoding="utf-8")
students = []
for s in file:
     name,age = s.strip().split(",")
     students.append({"name":name,"age":int(age)})    
file.close()
def add_student():
        name = input("姓名")
        age = int(input("年龄"))
        if name == "":
               print("姓名不能空")
               return        
        for a in students:
               if a["name"] == name:
                 print("该学生已存在")
                 break        
        else:  
            students.append({"name":name,"age":age})
            print("添加成功")
def remove_student():
       name = input("请输入删除学生的姓名")
       for c in students:
         if c["name"] == name:
           students.remove(c)
           print("删除成功")
           break
       else:
            print("该学生不存在")
def show_student():
         for d in students :
            print(f'姓名：{d["name"]}\n年龄:{d["age"]}\n') 
def find_student():
     name = input("请输入姓名")
     for e in students:     
         if e["name"] == name:
            print(f'姓名:{e["name"]}\n年龄:{e["age"]}')
            break
     else:
          print("该学生不存在")   
def xiu_students():
     name = input("请输入姓名")
     for e in students:     
         if e["name"] == name: 
             newage = int(input("请输入新年龄"))
             e["age"] = newage
             print("修改成功")
             break
     else:
          print("该学生不存在")    
def baocun_students():
        file = open("students.txt","w",encoding="utf-8")
        for s in students:
             file.write(f'{s["name"]},{s["age"]}\n')
        file.close()                                                
while True:
    b = (input("请输入操作：\n1.添加学生\n2.删除学生\n3.查看学生\n4.查找学生\n5.修改学生年龄\n6.退出"))
    if b ==  "1": 
         add_student()
    elif b == "2":
         remove_student()
    elif b == "3":          
            show_student()
    elif b == "4":
            find_student()
    elif b == "5":
             xiu_students()      
    elif b == "6":
       baocun_students()
       print("退出")
       break 
              
