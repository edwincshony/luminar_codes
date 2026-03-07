
def remove_stop_words(sentence):

    fr = open("13. ErrorHandling\\stopwords.txt")

    stop_words = [line.strip() for line in fr]

    # using join , approach 1 , best approach

    cleaned_words = [w for w in sentence.split(" ") if w not in stop_words]


    result = " ".join(cleaned_words)

    # approach 2

    # result = ""

    # for w in sentence.split():
    #     if w not in stop_words:
    #         result += w + " "

    return result

# sentence = "machine learning is a subset of AI"

sentence = "django is a one of python framework"

# assert remove_stop_words(sentence) == "machine learning subset AI","test case 1 failed"

assert remove_stop_words(sentence) == "django one python framework","test case 2 failed"

print("code accepted")