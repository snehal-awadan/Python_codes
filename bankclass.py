# Bank management system: bankclass

from abc import ABC,abstractmethod

class Account(ABC):
    cnt = 1         #static variable

# generates a unique account number based on the account type 
    @staticmethod
    def __generatecode(actype):
        acno = actype + str(Account.cnt)
        Account.cnt = Account.cnt+1
        return acno
    
    def __init__(self,name="",pin=0,balance=0.0,actype =""):
        self.__acno = Account.__generatecode(actype)
        self.__name = name
        self.__pin = pin
        self.__balance = balance

    def get_acno(self):
        return self.__acno
    
    def set_name(self,name):
        self.__name = name
        
    def get_name(self):
        return self.__name

    def set_pin(self,pinno):
        self.__pin = pinno
        
    def get_pin(self):
        return self.__pin

    def set_balance(self,balance):
        self._balance = bal
        
    def get_balance(Self):
        return self.balance

    def __str__(self):
        return f"Account No : {self.__acno} \nName: {self.__name}\nBalance: {self.__balance}"

# this function is same in all child class with differet action, so make it as abstract
    @abstractmethod
    def withdrawl(self):
        pass

class Saving(Account):
    intrest_rate_s = 0.4
    minbals = 50000.00

    def __init__(self, name="", pin=0, balance=0.0, ecs = 0.0, actype ="S"):
        super().__init__(name,pin,balance,actype)
        self.__ecs = ecs

    def set_ecs(self,ecs):
        self.__ecs = ecs
        
    def get_ecs(self):
        return self.__ecs

    def get_minbal(self):
        return Saving.min_bal_s
    
    def __str__(self):
        return super().__str__() +f"\nECS: {self.__ecs}"

    def withdrawl(self,amt):
        a = self.balance
        b = Saving.minbals

        if(a-amt)>b:
            self.set_balance(a-amt)
            return True
        else:
            return False

class Current(Account):
    intrest_rate = 0.5
    min_bal_c = 1000.00

    def __init__(self,name="", pin=0, balance=0.0, transaction =0, actype="C"):
        super().__init__(name,pin,balance,actype)
        self.__transaction = transaction

    def set_transaction(self,trans):
        self.__transaction = trans

    def get_transaction(self):
        return self.__transaction
    
    def __str__(self):
        return super().__str__ ()+ f"\nNo. of transaction : {self.__transaction}"

    def withdrawl(self,amt):
        a = self.__balance

        if a - amt > Current.min_bal_c:
            self.set_balance(a-amt)
            return True
        else:
            return False
        
class Demat(Account):
    intrest_rate = 0.6
    min_bal_D = 1000.00

    def __init__(self,name="", pin=0, balance=0.0, transaction =0,com =0.0, actype="D"):
        super().__init__(name,pin,balance,actype)
        self.__com = com

    def set_com(self,commission):
        self.__com = commission
        
    def get_com(self):
        return self.__commission
    
    def __str__(self):
        return super().__str__()+f"\ncommission: {self.__com}"

    def withdrawl(self,amt):
        a = self._balnce
        if a - amt > min_bal_D:
            return True
        else:
            return False

# create obj:
if __name__ == "__main__":
    ob = Saving("abc",1001,4000.00,20.00)
    print(ob)

    ob1 = Current("xyz",1050,4050.00,6)
    print(ob1)

    ob3 = Demat("pqr",1451,7560.00,20.00)
    print(ob3)
    
    
            



































    
