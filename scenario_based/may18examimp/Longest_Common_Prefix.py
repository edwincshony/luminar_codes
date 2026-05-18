# https://leetcode.com/problems/longest-common-prefix/description/

# def longestCommonPrefix(strs):
#     if not strs:
#         return ""

#     strs.sort()
#     s = ""
#     i = 0

#     while i < len(strs[0]):
#         if strs[0][i] == strs[-1][i]:
#             s += strs[0][i]
#         else:
#             break
#         i += 1

#     return s

# print(longestCommonPrefix(strs = ["dog","racecar","car"]))

strs = ["flower","flow","flight"]

strs.sort()

first,last = strs[0],strs[-1]

res = ""
i = 0
while i < len(first):

    if first[i] == last[i]:
        res += first[i]
        i += 1
    else:
        break

print(res)
