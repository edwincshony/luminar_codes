numbers = [10,20,11,12,20,10,13]

duplicate = []

for num in numbers:
        
        if numbers.count(num) > 1 and num not in duplicate:
                
            duplicate.append(num)

print(duplicate)

#using set below solution

# numbers = [10,20,11,12,20,10,13]

# st=set()

# for num in numbers:
        
#         if numbers.count(num) > 1:
                
#             st.add(num)

# print(st)