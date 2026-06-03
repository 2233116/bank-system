from random import choice
students = [
    {"name":"张三","age":18},
    {"name":"李四","age":19},
    {"name":"王五","age":20}
]
a = choice(students)
print(f'恭喜{a["name"]}被抽中\n年龄:{a["age"]}')