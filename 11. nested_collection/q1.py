# numbers from 1 to 10 list using comprehension

numbers_lst = [i for i in range(1,11)]

print(numbers_lst)
print("...................")

#nums = [2,4,6,8,10]
# create a new list that contains double of each number

nums = [2,4,6,8,10]
double = [num * 2 for num in nums]

print(double)
print("...................")

#create a list of even numbers from range of 20 to 50

evens = [i for i in range(20,51) if i % 2 == 0]

print(evens)

print("...................")
#create a new list that contain word length > 3

words = ["apple","bat","carrot","elephant","ball","red"]

word_len_gre_three = [w for w in words if len(w) > 3]

print(word_len_gre_three)
