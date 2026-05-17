"""
Longest Common Prefix
Easy
Topics
premium lock icon
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

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
