# 7. W.A.P to display product of even numbers and sum of odd numbers from 10 to 20

even_pro = 1
odd_sum = 1

for i in range(10,21):

    if i % 2 == 0:

        even_pro *= i

    else:

        odd_sum += i

print("product of even numbers",even_pro)
print("sum of odd numbers",odd_sum)