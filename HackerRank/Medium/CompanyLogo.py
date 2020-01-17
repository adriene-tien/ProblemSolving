# HackerRank Medium
# Company Logo Question: String analysis, character counting
# Currently O(n) time complexity where n = number of characters in the string. Currently looping through all.
# O(1) space complexity, dict caps out at 26 letters

if __name__ == '__main__':
    s = input()
    charDict = {}  # key: character, value: # of occurrences
    for i in range(len(s)):
        if s[i] not in charDict:
            charDict[s[i]] = 1
        else:
            charDict[s[i]] += 1

    top3count = 0
    sortedDict = sorted(charDict.items(), key=lambda x: (-x[1], x[0]))
    for v in sortedDict:
        if top3count < 3:
            print(v[0], charDict[v[0]])
        else:
            break
        top3count += 1