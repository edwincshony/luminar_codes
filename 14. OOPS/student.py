class Student:

    name: str
    course: str
    roll: int

    def set_student(self,name,course,roll):

        self.name = name # when initialized they are attributes
        self.course = course
        self.roll = roll

        # initialize attributes of an instance ie, constructor

    def display(self):

        print(self.name,self.course,self.roll)

edwin_instance = Student()

sreerag_instance = Student()


edwin_instance.set_student("edwin","Btech",22)
sreerag_instance.set_student("sreerag","Btech",21)

edwin_instance.display()
sreerag_instance.display()