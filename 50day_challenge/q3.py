# # Day 3: Register Check

# Write a function called `register_check` that checks how many students are in school. The function takes a dictionary as a parameter. If the student is in school, the dictionary says `'yes'`. If the student is not in school, the dictionary says `'no'`. Your function should return the number of students in school. Use the dictionary below. Your function should return `3`.

# python
# register = {
#     'Michael': 'yes',
#     'John': 'no',
#     'Peter': 'yes',
#     'Mary': 'yes'
# }





def register_check(register):

    count = 0
    for val in register.values():

        if val == "yes":

            count += 1
    return count
print(register_check(register = {
    'Michael': 'yes',
    'John': 'no',
    'Peter': 'yes',
    'Mary': 'yes'
}))