def analyse_numbers(*args,**kwargs):

    action = kwargs.get("action")

    if action == "max":

        return max(args)
    
    elif action == "min":

        return min(args)
    
print(analyse_numbers(10,20,30,action="min"))