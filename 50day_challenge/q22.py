def add_hash(text):

    return "#".join(text)

def add_underscore(text):

    return text.replace("#","_")

def remove_underscore(text):

    return text.replace("_","")

print(remove_underscore(add_underscore(add_hash('Python'))))