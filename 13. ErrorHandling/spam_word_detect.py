def spam_word_count(message):

    count = 0

    fr = open("13. ErrorHandling\\spam_words.txt")

    spam_words = [line.strip() for line in fr]

    #new_list = [expression for item in iterable if condition] 

    for w in message.split(" "):

        if w in spam_words:

            count += 1

    return count

print(spam_word_count("bonus cash edwin debt"))