# LeetCode Easy
# Remove vowels from a string question
# O(n) time complexity as we go through the size of the string
# Space complexity:

class Solution:

    def removeVowels(self, S: str) -> str:
        noVowels = ""
        vowels = ["a", "e", "i", "o", "u"]
        for i in range(0, len(S)):
            if S[i] in vowels:
                continue
            else:
                noVowels += S[i]

        return noVowels
