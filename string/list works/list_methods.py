"""class list:

    def append(self,object) add object at end of the list

    def insert(self,) insert new object at specified index

    def pop(self,index=-1) remove and return specified element at index
    
    def remove(self,object)  remove first occurence of object

    def count(self,object) frequency of object in the list

    def sort(self,reverse=False)

    def reverse()

    def extend(self,iterable) 
    """
    #      -3     -2     -1
colors = ["red","green","blue","green"]

    #       0      1      2

# colors.append("black")

# print(colors)

# colors.insert(2,"yellow")

# print(colors)

# removed_element = colors.pop(2)

# print(removed_element)

# colors.remove("green")

# print(colors)

freq = colors.count("ui")

print(freq)

akash_fvt_colors = ["red","white","blue","black"]

sree_fvt_colors = akash_fvt_colors.copy()

sree_fvt_colors[0] = "yellow"
# print(akash_fvt_colors)
# print(sree_fvt_colors)

# identity operator "is" is used to check if identity of two variables are same 

# if same object = True
# if different object = false

# print(akash_fvt_colors == sree_fvt_colors) # true => value compare

# print(akash_fvt_colors is sree_fvt_colors) #False => memory location compare

# numbers = [10,50,1,16,59,12,547]

# numbers.sort()

# print(numbers)

# numbers.sort(reverse=True)

# print(numbers)

# colors.reverse()

# print(colors)

colors = ["red","blue","black"]

new_colors = ["cyan","yellow"]

colors.append(new_colors) # ['red', 'blue', 'black', ['cyan', 'yellow']]

colors.extend(new_colors) # ['red', 'blue', 'black', 'cyan', 'yellow']

print(colors)






