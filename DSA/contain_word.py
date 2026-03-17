# approach 1

source = "traviduxtechnology"

target = "vridautx"

is_present = True

for ch in target:

    if ch not in source:

        is_present = False
        break

print(is_present)

# approach 2 (unique)

source = "traviduxtechnology"

target = "vridautx"

source_set = set(source)
target_set = set(target)

result = target_set.issubset(source_set)
print(result)