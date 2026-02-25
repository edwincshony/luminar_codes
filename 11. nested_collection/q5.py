# word count

text = "python programming programming is simple"

words = text.split(" ")

word_count = {w:words.count(w) for w in words}

print(word_count)