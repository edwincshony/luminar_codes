word = "aman##aplan**panamawith2car1bike"

# w.a.p to display alphabet_count, digit_count, special_character_count

special_character_count = 0
alpha_count = 0
digit_count = 0

for ch in word:

    if ch.isalpha():

        alpha_count = alpha_count + 1

    elif ch.isdigit():

        digit_count = digit_count + 1

    elif not ch.isalnum(): #check if not in alphabet and number ie special characters

        special_character_count = special_character_count + 1

print(f"Alphabet count is: {alpha_count}")
print(f"Digit count is: {digit_count}")
print(f"Special Characters count is: {special_character_count}")



