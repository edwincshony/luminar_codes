def capitalize(string):

    return " ".join(word.capitalize() for word in string.split(" "))

print(capitalize("i like learning"))