class Language:

    def __init__(self,l_name):

        self.l_name = l_name

    def display(self):

        print(self.l_name)
    
class FrameWork(Language):

    def __init__(self,l_name,f_name):

        super().__init__(l_name)

        self.f_name = f_name

    def display(self):
        
        super().display()

        print(self.f_name)


framework_instance = FrameWork("Python","Django")   

framework_instance.display()
