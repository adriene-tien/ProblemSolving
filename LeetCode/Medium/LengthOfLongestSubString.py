class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, length, maxLength = (0, 0, 0, 0)
        checkLetter = {}
        for i in range(len(s)):
            while s[right] not in checkLetter:
                checkLetter[s[right]] = 1
                right += 1
                length += 1
                if length >= maxLength: 
                    maxLength = length
                if right == len(s): 
                    break
            if right == len(s): 
                break 
            del checkLetter[s[left]]
            left += 1
            length -= 1

        return maxLength
            