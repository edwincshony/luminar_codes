def analyse_numbers(*args,**kwargs):

    action = kwargs.get("action")

    if action == "max":

        return max(args)
      
    if action == "min":

        return min(args)
      
    if action == "count":

        # count = 0

        # for num in args:

        #     count += 1

        # return count

        return len(args)
      
print(analyse_numbers(10,20,30,action="max"))
print(analyse_numbers(10,20,30,action="min"))
print(analyse_numbers(10,20,30,action="count"))
