def longestCommonPrefix(strs):

    s=""
    i=0
    while i < len(strs[0]):

        if strs[0][i] == strs[-1][i]:

            s += strs[0][i]
        
        else:
            break
        i += 1

    return s
print(longestCommonPrefix(strs = ["flower","flow","flight"]))
