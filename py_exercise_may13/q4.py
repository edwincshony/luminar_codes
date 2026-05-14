# 4. Display sum of even numbers from 50 to 100

even_tot = 0

for i in range(50,101):

    if i % 2 == 0:

        even_tot += i

print(even_tot)