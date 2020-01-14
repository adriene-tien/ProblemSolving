# HackerRank Medium
# CompanyLogo Question: String analysis, character counting
# Currently O(n) time complexity,
# O(1) storage complexity, dict caps out at 26 letters

# Come back to this one. There are better implementations

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    charDict = {}  # key: character, value: # of occurrences
    for i in range(len(s)):
        if s[i] not in charDict:
            charDict[s[i]] = 1
        else:
            charDict[s[i]] += 1

    top3count = 0
    sortedDict = sorted(charDict.items(), key=lambda kv: (-kv[1], kv[0]))
    for v in sortedDict:
        if top3count < 3:
            print(v[0], charDict[v[0]])
        else:
            break
        top3count += 1