class Student:
    def __init__(self,principal,vice_principal,t_students,total_classes):
        self.total_teachers={}
        self.principal=principal
        self.vice_principal=vice_principal
        self.total_students=t_students
        self.total_classes=total_classes
        self.total_staff={}
    def add_teachers(self,name,subject):
        self.total_teachers[name]=subject
    def left_teachers(self,nam):
        if nam in self.total_teachers:
            del self.total_teachers[nam]
        else:
            print("There is no teacher with the name of",nam)   
    def add_staff(self,naam,role):
        self.total_staff[naam]=role
    def new_viceprincipal(self,vice_principal):
        self.vice_principal=vice_principal
    def new_principal(self,principal):
        self.principal=principal
    def left_staff(self,n):
       if n in self.total_staff:
            del self.total_staff[n]
       else:
          print("There is no staff with the name of",n)   
    def print_teachers(self):
        print("**************Total teachers**************")
        for name,subject in self.total_teachers.items():
            print("Name:",name,",","Subject:",subject)
    def print_staff(self):
        print("**************Total staff**************")
        for naam,role in self.total_staff.items():
            print("Name:",naam,",","Role:",role)
    def printme(self):
        print("Principal:",self.principal)
        print("Vice Principal:",self.vice_principal)
        print("Total students:",self.total_students)
        print("Total classes:",self.total_classes)
stu=Student("no","Mr.Vikrant sharma",300,12)
stu.printme()
stu.add_teachers("Omveer sir","English")
stu.add_teachers("Vikrant sir","Maths")
stu.add_teachers("Gaurav sir","Physics")
stu.add_teachers("Gajendra sir","Chemistry")
stu.add_teachers("Naveeta mam","Biology")
stu.add_teachers("Richa mam","Social science")
stu.add_teachers("Gargi mam","Economics")
stu.add_teachers("Anuranjan sir","Hindi")
stu.add_teachers("Anuranjan sir","Sanskrit")
stu.print_teachers()
stu.add_staff("Mr. aniket ","Guard")
stu.add_staff("Mr. Manoj","Sweeper")
stu.add_staff("Mr. bhagwati","cleaner")
stu.print_staff()
stu.left_teachers("Omveer sir")
stu.print_teachers()
stu.left_staff("Mr. Manoj")
stu.print_staff()