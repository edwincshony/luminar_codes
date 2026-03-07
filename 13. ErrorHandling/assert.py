# assert condition,"error message"

def cube(num):

    result = 27 # purposely given 27 to fail #if result = num **3 no errors

    return result

assert cube(3) == 27,"test case1 failed" #if False AssertionError occurs
assert cube(4) == 64,"test case2 failed"

print("code accepted")

def max_two(n1,n2):

    result = 1

    if n1>n2:
        result = n1

    else:
        result = n2

    return result

assert max_two(10,20)==20,"test case1 failed"
assert max_two(-5,10)==10,"test case2 failed"

print("code accepted")