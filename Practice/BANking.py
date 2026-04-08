class bankaccount:
    def __init__(self,account_num,balance=0):
        self.account_num=account_num
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"amout succesfuly depositedcurrent amount{self.balance:.2f}")
        else:
            print("number is camt be nega")
    def withdraw(self,amount):
        if amount>0:
            if self.balance>=amount:
                self.balance-=amount
                print(f"amout succesfuly withdraw current amount{self.balance:.2f}")
            else:
                return "incuffecient balance"
        else:
            print("num bant be negative")
    def cheak_balance(self):
        print(f"balance os {self.balance:.2f}")
if __name__=="__main__":

    p=bankaccount("55464",100)
    while True:
        print("1.deposit\n2.view balance.\n3.cheak_balance\n4.exit")
        choise=input("Eter action")
        if choise=="3":
            p.cheak_balance()
        elif choise=="1":
            amount=float(input("Enter ur amount"))
            p.deposit(amount)
        elif choise=="2":
            amount=float(input("Enter ur amount"))
            p.withdraw(amount)
        else:
            print("bye")
            break
    

        

