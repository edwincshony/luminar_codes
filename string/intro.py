# -----------------------------
# Basic data types
# -----------------------------

address = """address line 1
address line 2"""
number = 732
is_active = True
avg = 4.6

# Checking data types
print(type(address))     # <class 'str'> # 'address' is an object of class str
print(type(number))      # <class 'int'> # 'number' is an object of class int
print(type(is_active))   # <class 'bool'> # 'is_active' is an object of class bool
print(type(avg))         # <class 'float'> # 'avg' is an object of class float


# -----------------------------
# String object and methods
# -----------------------------

word = "luminarch Technolab Technohub"

# 'word' is an object of class str
# Methods like upper(), casefold(), find(), etc. belong to the str class


"""
Simplified view of the str class (not actual implementation):

class str:
    def casefold(self):
        pass

    def capitalize(self):
        # Return a capitalized version of the string
        pass

    def index(self, substr):
        # Return index of substr; raise ValueError if not found
        pass

    def find(self, substr):
        # Return first index of substr; return -1 if not found
        pass

    def rfind(self, substr):
        # Return last index of substr; return -1 if not found
        pass

    def count(self, substr):
        # Return number of occurrences of substr
        pass
"""


# -----------------------------
# String method usage
# -----------------------------

print(word.upper())          # Convert all characters to uppercase
print(word.casefold())       # Case-insensitive lowercase conversion

print(word.index("lu"))      # Index of "lu" from the left; raises ValueError if not found
print(word.find("lu"))       # Index of "lu" from the left; returns -1 if not found
print(word.rfind("ch"))      # Index of "ch" from the right; returns -1 if not found
print(word.count("Tech"))    # Number of times "Tech" appears



