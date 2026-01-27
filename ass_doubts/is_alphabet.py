char = input("enter the alphabet: ")

ascii_value = ord(char)

        #lower_case check               #upper_case check

if ascii_value in range(97,123) or ascii_value in range (65,91):
# if "a" <= char <= "z" or "A" <= char <= "Z":
    print("alphabet")

else:
    print("not alphabet")