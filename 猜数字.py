import random
answer = random.randint(1,100)
a = answer + 1
b  = answer - 1
print(answer)
count = 0
while True:
    z = int(input("请输入数字"))
    count += 1        
    if  z >=  a :
        print("大了")
        
    elif z <= b:
        print("小了")
        
    elif z == answer:
        print("猜对了")
        break

print(f'你猜了{count}')