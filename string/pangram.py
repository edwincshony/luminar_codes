#pangram

"""
Use return when you are done with the function
Use break when you are done with the loop but not the function
"""


# word_name = "The quick brown fox jumps over the lazy dog"

# alphabet = "abcdefghijklmnopqrstuvwxyz"

def is_pangram(word_name):

    alphabets = "abcdefghijklmnopqrstuvwxyz"

    for alphabet in alphabets:

        if alphabet not in word_name:

            return False
        
    return True

# print(is_pangram(word_name="The quick brown fox jumps over the lazy dog"))



def is_pangram_using_str_mehtods(word_name):

    alphabets = "abcdefghijklmnopqrstuvwxyz"

    for alphabet in alphabets:

        if word_name.count(alphabet) == 0:

            return False
        
    return True

print(is_pangram(word_name="The quick brown fox jumps over the lazy dog"))