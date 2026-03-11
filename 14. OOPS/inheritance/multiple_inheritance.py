# 3. Multiple Inheritance
# A child class inherits from more than one parent class.
# multiple inheritance not supported in java and javascript so interface used

class Father:

    def coaching_skill(self):

        print("coaching skill")

    def cooking_skill(self):

        print("father cooking skill")

class Mother:

    def cooking_skill(self):

        print("mother cooking skill")

class Child(Father,Mother):

    pass

child_instance = Child()

child_instance.coaching_skill() # output: coaching skill

child_instance.cooking_skill() # output: father cooking skill, because Father class was first in inheritance order