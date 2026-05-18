# This code checks whether the string note can be formed using the letters from magazine.

note = "aabb"
magazine = "ab"

magazine_freq = {}

for l in magazine:

    if l in magazine_freq:

        magazine_freq[l] += 1

    else:

        magazine_freq[l] = 1

for l in note:

    if l in magazine_freq and magazine_freq[l] > 0:

        magazine_freq[l] -= 1

    else:

        print("not ransome")
        break

else:
    print("ransome")