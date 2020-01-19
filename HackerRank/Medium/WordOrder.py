# HackerRank Medium
# Word Order question: Repeated words, string segments
# O(n) time complexity, have to go through n input words coming from STDIN
# O(n) space complexity, worst case every word is unique

from sys import stdin

num_words = int(input())
word_dict = {}
distinct_words = 0

for i in range(0, num_words):
    word = input()
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
        distinct_words += 1

print(distinct_words)
for word in word_dict.keys():
    print(word_dict[word], end=" ")
