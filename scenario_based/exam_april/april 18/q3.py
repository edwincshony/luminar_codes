# first 10 prime numbers

num = 2

count = 0

while count < 10:

    is_prime = True

    for i in range(2,num):

        if num%i == 0:

            is_prime = False

            break

    if is_prime:

        print(num,end=" ")
        count += 1 #You only increment count when a prime is found.
                    #If you incremented count outside the if, you'd count every number, not just primes → wrong result.

    num += 1 #So num keeps increasing each loop iteration.