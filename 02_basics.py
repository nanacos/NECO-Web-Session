class NecobishiBank():

    balance = 0
    def __init__(self, balance):
        self.balance = balance 
    
    def withdraw(self,amount):
        print("100万引き出せた")

    def send(self, amount):
        #self（自分の口座から）
        print("100万送った")

    def deposit(self, amount):
        print("100万預けた")



shonandai_atm = NecobishiBank(100)
#ねこびしのデータが湘南台ATMに
shonandai_atm.withdraw(10)
print(shounandai_atm.balance)

yokohama_atm = NecobishiBank(1000)
print("横浜ATM：" + str(yokohama_atm.balance)