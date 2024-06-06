# Person oops:

class Person:
    #create constructor
    def __init__(self,pid = 0,pname="",mob=""):
        #initialize the data members
        self.__pid = pid
        self.__pname = pname
        self.__mobile = mob
        
    def __str__(self):
        return f"Id: {self.__pid} name: {self.__pname} mobile: {self.__mobile}"

    def set_pid(self,pid):
        self.__pid = pid

    def get_pid(self):
        return self.__pid

    def set_pname(self,pname):
        self.__pname = pname
    def get_pname(self):
        return self.__pname

    def set_mobile(self,mobile):
        self.__mobile = mobile

    def get_mobile(self):
        return self.__mobile

p1=Person(12,"andb",2357683)
print(p1)
        
