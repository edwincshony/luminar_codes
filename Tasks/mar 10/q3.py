"""
3. Create a class Employee with a constructor that initializes employee name and salary. Display the employee details.

"""

class Employee:

    def __init__(self,e_name,e_salary):

        self.e_name = e_name
        self.e_salary = e_salary

    def display(self):

        print(self.e_name,self.e_salary)

edwin_instance = Employee("Edwin",30000)

edwin_instance.display()

