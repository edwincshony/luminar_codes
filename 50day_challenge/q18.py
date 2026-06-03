def any_number(*args):

    tot = 0

    for num in args:

        tot += num
    
    average = tot/len(args)

    return average

print(any_number(12,90))