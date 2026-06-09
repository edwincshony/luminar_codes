def all_the_same(ct):

    for i in ct:

        if i.lower() != ct[0].lower():

            return False    
        
    return True

print(all_the_same(['Mary','Mary','Mary']))
print(all_the_same(['Mary','Mary','John']))