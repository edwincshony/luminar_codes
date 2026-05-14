num = 2
prime_nums = []
count = 0
n = 10

while count < 10:

            is_prime = True

            for i in range(2,num):

                if num%i == 0:

                    is_prime = False

                    break

            if is_prime:

                if count < 10:
                    prime_nums.append(num)
                count += 1 
                #You only increment count when a prime is found.
                            #If you incremented count outside the if, you'd count every number, not just primes → wrong result.

            num += 1 #So num keeps increasing each loop iteration.

print(len(prime_nums))