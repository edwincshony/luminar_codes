"""
class tuple:

    def count(self,value) count the frequency of value appeared in tuple
        
    
    def index(self,value) returns index of first occurence of value
    

"""


prices = (200,300,400,300)

#indexing uses square brackets
# prices[0] = 100 # TypeError: 'tuple' object does not support item assignment


print(prices.count(300))
print(prices.index(300))

#create a tuple and store ur age only

my_age = (22)

print(type(my_age)) #<class 'int'>

my_age = (22,)

print(type(my_age)) #<class 'tuple'>



