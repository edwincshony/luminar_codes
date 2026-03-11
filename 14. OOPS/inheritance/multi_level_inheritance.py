"""
2. Multi-Level Inheritance
A class inherits from another class, which already inherited from another class.
Grandparent → Parent → Child
"""

class GrandParent:

    def properties(self):

        print("grand parent properties")

class Parent(GrandParent):

    def house(self):

        print("parent house method")

class Child(Parent):

    pass

child_instance = Child()

child_instance.house()
child_instance.properties()