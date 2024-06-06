# Assign_08
#Q. 1)

class Student:
    def __init__(self,name,m1,m2,m3,sid):
        self.__sid = sid
        self.__name = name
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3
        
    #to return the data
    def __str__(self):
        return f"id: {self.__sid}\n name:{self.__name}\n m1:{self.__m1}\n m2:{self.__m2}\n m3:{self.__m3}\n"

    #getter and setter:
    def set_sid(self,sid):
        self.__sid = sid
    def get_sid(self):
        return self.__sid

    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_m1(self,m1):
        self.__m1 = m1
    def get_m1(self):
        return self.__m1

    def set_m2(self,m2):
        self.__m2 = m2
    def get_m2(self):
        return self.__m2

    def set_m3(self,m3):
        self.__m3 = m3
    def get_m3(self):
        return self.__m3

#create object;
s1 = Student("abc",98,70,68,1)
print(s1)
s2 = Student("xyz",96,81,96,2)
print(s2)
