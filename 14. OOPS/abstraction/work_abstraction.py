from abc import ABC,abstractmethod

class Editor:

    @abstractmethod
    def open(self): pass

    @abstractmethod
    def execute(self): pass

    @abstractmethod
    def debug(self): pass

class VsCode(Editor):

    def open(self):

        print("Vs code open")

    def execute(self):

        print("Vs code execute")

    def debug(self):

        print("Vs code debug")

vs_code_inst = VsCode()

vs_code_inst.open()
vs_code_inst.execute()
vs_code_inst.debug()