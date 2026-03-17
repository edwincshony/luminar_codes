"""5. Create a class Employee with a method work(). Create subclasses Developer and Manager that override the work() method.
"""

class Employee:

    def work(self):

        print("employee is working")

class Developer(Employee):

    def work(self):

        print("developer is working")

class Manager(Employee):

    def work(self):

        print("manager is working")

dev_inst = Developer()
dev_inst.work()
man_inst = Manager()
man_inst.work()