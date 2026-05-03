"""
3. Flatten Nested List
data = [1, [2, [3, 4], 5], 6]
Task: Convert it into a single flattened list:
[1, 2, 3, 4, 5, 6]
"""

data = [1, [2, [3, 4], 5], 6]

def flatten(data):
    flat_list = []

    for element in data:

        if type(element) is list:

            flat_list.extend(flatten(element))
        else:
            flat_list.append(element)
    return flat_list

print(flatten(data))

# “Where is the base case?”
#“When the element is not a list, we stop recursion and append it directly.”