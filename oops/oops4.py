class Employee:
    def __init__(self,name,id,department,salary):
        self.name=name
        self.id=id
        self.department=department
        self.salary=salary    
    def wages(self,working_hours):
        if working_hours>8:
            self.salary=self.salary+working_hours/2
        else:
            self.salary=self.salary
    def dep(self,depart):
        self.department=depart
    def employee_details(self):
        print("Name:",self.name)
        print("id:",self.id)
        print("Department:",self.department)
        print("Salary:",self.salary)
        print("-------------------------")


EMPLOYEE1=Employee("Akshay",324,"RESEARCH",25000)
EMPLOYEE1.wages(40)
EMPLOYEE1.employee_details()
EMPLOYEE2=Employee("Manvar",898,"ACCOUNTING",15000)
EMPLOYEE2.wages(65)
EMPLOYEE2.employee_details()
EMPLOYEE3=Employee("Naitik",1298,"SCIENCE",15000)
EMPLOYEE3.wages(65)
EMPLOYEE3.employee_details()
print("NEW DEPARTMENT")
EMPLOYEE3.dep("COMPUTING")
EMPLOYEE3.employee_details()