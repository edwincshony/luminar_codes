def biggest_odd(number):

    odd_digits = [int(digit) for digit in number if int(digit) % 2 != 0]

    if odd_digits:
        return max(odd_digits)
    else:
        return None

print(biggest_odd("23569"))
print(biggest_odd("26"))