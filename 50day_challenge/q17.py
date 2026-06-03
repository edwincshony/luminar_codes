# **Day 17: User Name Generator**

# Write a function called **user_name**, that creates a username for the user. The function should ask a user to **input** their name. 
# The function should then reverse the name and attach a randomly issued number between 0 – 9 at the end of the name. The function should return the **username**.

import random  # Step 1: Import the random module


def user_name():
    name = input("Enter the name: ")

    rev_name = name[::-1]

    # Step 2: Generate a single random number between 0 and 9
    # We wrap it in str() because we can only concatenate strings to strings
    random_num = str(random.randint(0, 9))

    # 1. **`random.randint(0, 9)`** – Picks a single random whole number from 0 to 9 (e.g., `7`).
    # 2. **`str(...)`** – Converts that number into text (e.g., `7` becomes `"7"`). This is necessary because Python cannot glue raw numbers to text.
    # 3. **`random_num =`** – Saves that text character into a variable, ready to be attached to the end of the reversed name.

    # Step 3: Combine them
    username = rev_name + random_num

    return username


print(user_name())

