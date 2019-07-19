# codesignal
def firstNotRepeatingCharacter(s):
    result = "_"
    dictionary = {}
    for i,c in enumerate(s):
        if c in dictionary.keys():
            dictionary[c] = -1
        else:
            dictionary[c] = i
    min_key = len(s)+1
    for k in dictionary.keys():
        if dictionary[k]>=0:
            min_key = min(min_key,dictionary[k])
            result = s[min_key]
    return result
