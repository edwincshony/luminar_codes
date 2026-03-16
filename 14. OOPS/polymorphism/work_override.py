class Parent:

    def properties(self):

        print("solar 5kg gold 2 car")

    def weds_with(self):

        print("gopalan")

class Child(Parent):

    def weds_with(self):
        print("Dijo")

child_instan = Child()

child_instan.properties()
child_instan.weds_with()