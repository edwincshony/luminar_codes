#pangram

"""
Use return when you are done with the function
Use break when you are done with the loop but not the function
"""


                    # word_name = "The quick brown fox jumps over the lazy dog"

                    # alphabet = "abcdefghijklmnopqrstuvwxyz"

# def is_pangram(word_name):

#     alphabets = "abcdefghijklmnopqrstuvwxyz"

#     for alphabet in alphabets:

#         if alphabet not in word_name:

#             return False
        
#     return True

# print(is_pangram(word_name="The quick brown fox jumps over the lazy dog"))



# def is_pangram_using_str_mehtods(word_name):

#     ALPHABETS = "abcdefghijklmnopqrstuvwxyz"

#     for alphabet in ALPHABETS:

#         if word_name.count(alphabet) == 0:

#             return False
        
#     return True

# print(is_pangram_using_str_mehtods(word_name="The quick brown fox jumps over the lazy dog"))


# word = "The quick brown fox jumps over the lazy dog"

# ALPHABETS = "abcdefghijklmnopqrstuvwxyz"

# is_pangram = True

# for alphabet in ALPHABETS:

#     if alphabet not in word:

#         is_pangram = False

#         break

# print(is_pangram)



word = "The quick brown fox jumps over the lazy dog"

ALPHABETS = "abcdefghijklmnopqrstuvwxyz"

is_pangram = True

for alphabet in ALPHABETS:

    if word.find(alphabet) == -1:

        is_pangram = False

        break

print(is_pangram)