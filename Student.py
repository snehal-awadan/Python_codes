class Student:
    def __init__(self,stuid = 0, name="",m1=0,m2=0,m3=0,gpa=0.0):
        self.__stuid = stuid
        self.__name = name
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3
        self.__gpa = Student.calculategpa(self.__m1,self.__m2,self.__m3)

    def __str__(self):
        return f"Student Id: {self.__studid} \nName : {self.__name} \nM1 : {self.__m1} \nM2 : {self.__m2} \nM3 : {self.__m3}"

    #setter:
    def set_stuid(self,stuid):
        self.__stuid = stuid

    def set_name(self,name):
        self.__name= name

    def set_stuid(self,m1):
        self.__m1 = m1

    def set_m2(self,m2):
        self.__m2 = m2

    def set_m3(self,m3):
        self.__m3 = m3

    #getter:

    def get_stuid(self):
        return self.__stuid
    
    def get_name(self):
        return self.__name
    
    def get_m1(self):
        return self.__m1
    
    def get_m2(self):
        return self.__m2
    
    def get_m3(self):
        return self.__m3
    
    def calculategpa(m1,m2,m3):
        return float((1/3) *m1 + (1/2) *m2 +(1/4)*m3)


studlst = [Student(101, "Rahul", 67, 81, 73),
           Student(102, "Mitali", 89, 81, 56),
           Student(103, "Gaurav", 80, 90, 97)]



#function;
#Display all student.
def Display_all_student():
    for und in studlst:
        print(und)

#search by id
def search_by_id(id):
    for ind,ob in enumerate(studlst):
        if ob.getstuid() == id:
            return ind,ob
    return -1,None

#search_by_name()
search_by_name(name):
        for ind,ob in studlst:
            if ob.get_name == name:
               return ind,ob
        return -1,None

#calculate_gpa()
def calculate_gpa():
    marks = tuple(map(float,input("enter marks: "))).split()
    print(result)
    

choice = 0
while choice!=5:
    choice = int(input("""1. Display all student.
                          2. search by id.
                          3. search by name.
                          4. calculate gpa.
                          5. exit
                          enter your choice: """))
    match choice:
        case 1:
            Display_all_student()
        
        case 2:
            search_by_id()
            id = int(input("enter id to search: "))
            
        case 3:
            search_by_name()
            name = int(input("enter the name to search: ")
        
        case 4:
            calculate_gpa()
        
        case 5:
            print("existing from the program")
            
        case _:
            print("invalid choide")











































