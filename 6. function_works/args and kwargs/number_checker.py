def number_checker(*args,**kwargs):

    type = kwargs.get("type")

    if type=="odd":

        # count = 0

        # for num in args:

        #     if num % 2 != 0:

        #         # print(num)

        #         count += 1

        # return count

        odds = [num for num in args if num%2!=0]

        return len(odds)
    
    if type == "even":

        count = 0

        for num in args:

            if num % 2 == 0:

                # print(num)

                count += 1

        return count
    
    if type == "positive":

        count = 0

        for num in args:

            if num > 0:

                count += 1

        return count
    
    if type == "negative":

        count = 0

        for num in args:

            if num < 0:

                count += 1

        return count

print(number_checker(10,11,12,13,14,15,type="odd"))
print(number_checker(10,11,12,13,14,15,16,type="even"))
print(number_checker(10,11,12,13,14,15,16,type="positive"))
print(number_checker(10,11,12,13,14,-15,-16,type="negative"))

