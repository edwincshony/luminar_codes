st = {10,20,45,89}

#when indexing is not supprted then ordering not possible

# print(st[0]) # TypeError: 'set' object is not subscriptable

# st={} # dictionary

# creating object of class

# st=set() # empty set
# st=list() # empty list
# st=dict() # empty dict
# st=tuple() # empty tuple

# st.update((100,1))

# print(st)

# for num in st:

#     print(num)

# list => array
# set => hashset

colors = {"red","green","blue","blue","yellow"}

for c in colors:

    print(c)

"""
class set:

    def add(self,value) add an element to a set

    def union(self,set)

    def intersection(self,set)

    def difference()

    def issuperset()

    def issubset()



"""

print(dir(set))

foods = {"dosa","tea","coffee","friedrice"}

foods.add("cb")

print(foods)



set_a = {10,20,30,40,50}

set_b = {40,50,400,500,600}

union_set = set_a.union(set_b)

i_set = set_a.intersection(set_b)

diference_set = set_a.difference(set_b)

print(union_set)
print(i_set)
print(diference_set)

set3 = {10,20,30,40,50}

set4 = {30,40}

print(set3.issuperset(set4))
print(set4.issubset(set3))