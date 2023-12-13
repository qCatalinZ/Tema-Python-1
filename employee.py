class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):

    mgr_count = 0 

    def __init__(self, name, salary, departament):
        super().__init__(name, salary)
        self.departament = f"B06_{departament}"
        Manager.mgr_count+=1

    def display_employee(self):     # X % 3 == 0
        print("Name : ", self.name)

    def display_mgr_count(self):
        print(f"Total number of manager(s) is {Manager.mgr_count}")

# X = 6
# Y = 19

Employee1 = Employee("Ciprian", 2000)
Employee2 = Employee("Dana", 2050)
Employee3 = Employee("Cosmin", 3000)
Employee4 = Employee("Larisa", 1500)
Employee5 = Employee("Marian", 2900)
Employee6 = Employee("Mariana", 1000)

Employee1.display_employee()
Employee2.display_employee()
Employee3.display_employee()
Employee4.display_employee()
Employee5.display_employee()
Employee6.display_employee()

Employee6.display_emp_count()

ManagerI= []

Manager1 = Manager("Catalin", 60000, "McDonalds")
ManagerI.append(Manager1)
Manager2 = Manager("Ionut", 55000, "Dristor")
ManagerI.append(Manager2)
Manager3 = Manager("Antonel", 50000, "Profi")
ManagerI.append(Manager3)
Manager4 = Manager("Denisa", 45000, "Cora")
ManagerI.append(Manager4)
Manager5 = Manager("Alina", 40000, "Lidl")
ManagerI.append(Manager5)
Manager6 = Manager("Luminita", 35000, "Penny")
ManagerI.append(Manager6)

for i in ManagerI:
    i.display_employee()

ManagerI[0].display_emp_count()

ManagerI[0].display_mgr_count()