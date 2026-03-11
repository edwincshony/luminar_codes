# Polymorphism = "many forms", ability of an entity (like a function or object) to perform different actions based on the context.

# eg: +
    # 10 + 20 = 30
    # "hai" + "hello" = haihello

# 1) METHOD OVERLOADING = within same class same method name different number of parameters (not supported in Python) (use *args,**kwargs)


class Calculator:

    def add(self,n1,n2):

        return n1 + n2
    
    def add(self,n1,n2,n3):

        return n1 + n2 + n3
    
    def add(self,n1,n2,n3,n4):# only this add method with 4 para exist

        return n1 + n2 + n3 + n4 
        # In Python, when methods have the same name, the last definition overrides the previous ones.
    
cal_instance = Calculator()

print(cal_instance.add(10,20,30,40)) # ✅
print(cal_instance.add(100,200,300)) # TypeError: Calculator.add() missing 1 required positional argument: 'n4'
print(cal_instance.add(1000,2000))