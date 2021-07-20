class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_array = s.split()
        if len(str_array) > 0: 
            return len(str_array[-1])
        else: 
            return 0

# O(n) time due to use of split 
# O(n) space due to use of str_array. n would be number of words 