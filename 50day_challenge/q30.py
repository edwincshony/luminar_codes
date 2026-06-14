def repeated_name(names):

    counts = {}

    for name in names:

        if name in counts:

            counts[name] += 1

        else:

            counts[name] = 1

    most_repeated = max(counts, key=counts.get)

    return most_repeated

print(repeated_name(["John","Peter","John","Peter","Jones","Peter"]))

def sorted_names(names):
    result = []

    for name in names:
        first, last = name.split()
        result.append(f"{last} {first}")

    result.sort()

    return result


names = [
    "Beyonce Knowles",
    "Alicia Keys",
    "Katie Perry",
    "Chris Brown",
    "Tom Cruise"
]

print(sorted_names(names))