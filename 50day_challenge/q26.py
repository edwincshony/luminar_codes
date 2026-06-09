def sort_words(text):

    text = text.replace(" ","")

    return sorted(set(text))

print(sort_words("love life"))

