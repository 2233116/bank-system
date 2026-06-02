class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def show_balance(self):
        return self.balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("余额不足")
            return False
file = open("balance.txt","r")
c = int(file.read())
file.close()            
account1 = BankAccount("张三", c)
account2 = BankAccount("李四", 5000)
history = []
while True:
    choice = input("请输入操作：\n1.存款\n2.取款\n3.查看余额\n4.查看交易记录\n5.退出")
    if choice =="1":
        try:
           money1 = int(input("请输入存款金额："))
           account1.deposit(money1)
           history.append(f"存款{money1}")
        except:
            print("请输入正确数字")
    elif choice =="2":
            try:
              money2 = int(input("请输入取款金额："))
              success = account1.withdraw(money2)
              if success:  
                history.append(f"取款{money2}")
              else:
                 history.append(f"取款失败") 
            except:
                print("请输入正确数字")  
    elif choice =="3":
        print(f"当前余额：{account1.show_balance()}") 
    elif choice =="4":
        for item in history:
            print(item)

    elif choice == "5":
        file = open("balance.txt","w")
        file.write(str(account1.balance))
        file.close()
        break
    else:
        print("输入错误")          
print(account1.show_balance())
print(account2.show_balance())