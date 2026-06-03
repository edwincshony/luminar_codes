def count_words(sentence):

    count = 0

    for w in sentence.split(" "):

        count += 1
        
    return count

print(count_words("I love learning"))

def count_elements(sentence):

    count = 0

    for w in sentence:

        if w != " ":

            count += 1
        
    return count

print(count_elements("I love learning"))
    