def index_position(text):

    positions = []

    for i in range(len(text)):

        if text[i].islower():

            positions.append(i)

    return positions
       
print(index_position("LovE"))