class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person_info(self):
        print(f"name is {self.name}\n age is {self.age}")

class employee(person):
    def __init__(self,name,age,employee_id,salary):
        super().__init__(self,name,age)
        self.employee_id=employee_id
        self.salary=salary
    def display_employee_info(self):
        self.display_person_info()
        print(f"employee id is {self.employee_id}\nsalary is {self.salary}")
class manager(employee):
    def __init__(self,name,age,employee_id,salary,department):
        super().__init__(self,name,age,employee_id,salary)
        self.department=department
    def display_manager_info(self):
        self.display_employee_info()
        print(f"department is {self.department}")
if __name__=="__main__":
    while True:
        print("Choose the option:\n1.Add a pereson\n2.add em\n3.add man\n4.aexit ")
        choice=input("Enter you choise :-")
        if choice=="1":
            name=input("name")
            age=input("age")
            person1=person(name,age)
            person1.display_person_info()
        elif choice=="2":
            name=input("name")
            age=input("age")
            emoploy_id=input("id")
            salary=input("salaru")
            employee1=employee(name,age,emoploy_id,salary)
            employee1.display_employee_info()
        elif choice=="3":
            name=input("name")
            age=input("age")
            emoploy_id=input("id")
            salary=input("salaru")
            department=input("department")
            manager1=manager(name,age,emoploy_id,salary,department)
            manager1.display_manager_info()
        else:
            break

