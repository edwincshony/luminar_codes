def hide_password():

    password = input("Enter the password: ")

    hidden = "*" * len(password)

    print(hidden)

    return f"The Password is {len(password)} characters long"

print(hide_password())

