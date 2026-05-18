# Find Words That Can Be Formed by Characters

# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).

# Return the sum of lengths of all good strings in words.

 

# Example 1:

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:

# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

# def FindWords(words:list,char:str):
#     result=0
#     for note in words:
#         can_form=True
#         for ch in note:
#             if note.count(ch)>char.count(ch):
#                 can_form=False
#                 break
        
#         if can_form==True:
#             result+=len(note)

#     return result
# words = ["cat","bt","hat","tree"]
# char = "atach"

# print(FindWords(words,char))


words = ["cat","bt","hat","tree"]
char = "atach"
result=0
for note in words:
    can_form=True
    for ch in note:
            if note.count(ch)>char.count(ch):
# note.count(ch) → how many times the word needs the character
# char.count(ch) → how many times the character is available

# If needed > available, the word is impossible to build.
                can_form=False
                break
        
    if can_form==True:
            result+=len(note)

print(result)
