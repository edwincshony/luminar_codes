"""
class dict:

    def keys(self): return all keys

    def values(self): return all values

    def items(self): get key value pairs

    def get(self,key): get value by key

    def pop(self,key): remove specified key and value
"""

employee = {"id":101,"name":"edwin","salary":45000,"dept":"qa"}

for key in employee.keys():

    print(key)

for val in employee.values():

    print(val)

for key,val in employee.items():

    print(key,val)

print(dir(dict))

# employee.pop("dept")

# print(employee)

print(employee.get("email","dummy@gmail.com")) #return None if key doesnt exist, also return the second parameter if key doesnt exist

# print(employee["names"]) # become error if key doesnt exist






