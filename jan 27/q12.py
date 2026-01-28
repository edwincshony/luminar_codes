
print(ord("a"))
print(ord("b"))
print(ord("z"))

# ascii value not in 97 and 122 then not lowercase alphabet

print(ord("A"))
print(ord("B"))
print(ord("Z"))

# ascii value not in 65 and 90 then not uppercase alphabet


char = input("enter the alphabet: ")

ascii_value = ord(char)

        #lower_case check               #upper_case check

if ascii_value in range(97,123) or ascii_value in range (65,91):
# if "a" <= char <= "z" or "A" <= char <= "Z":
    print("alphabet")

else:
    print("not alphabet")