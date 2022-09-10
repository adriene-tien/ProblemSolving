# Leetcode medium 
# You are given a string s.
# A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is equal to s (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.
# Return the number of good splits you can make in s.

class Solution(object):

    # O(n) time complexity. two for loops where max iteration is n where n is length of s 
    # O(n+n+n) -> O(n) storage complexity, need s2 which will be n-1 in length at its most, char_dict1 and char_dict2 which will hold n elements max 
    def numSplits(self, s): 
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 1: 
            return 0 

        good_splits = 0
        s2 = s[1:len(s)]

        char_dict1 = {s[0]: 1}
        num_distinct1 = 1 

        char_dict2 = {}
        num_distinct2 = 0 
        for i in range(0, len(s2)): 
            if s2[i] not in char_dict2: 
                char_dict2[s2[i]] = 1 
                num_distinct2 += 1
            else: 
                char_dict2[s2[i]] += 1 
        
        for i in range(1, len(s)):
            if num_distinct1 == num_distinct2: 
                good_splits += 1 
                
            if s[i] not in char_dict1: 
                char_dict1[s[i]] = 1 
                num_distinct1 += 1
            
            char_dict2[s[i]] -= 1
            if char_dict2[s[i]] == 0: 
                num_distinct2 -= 1 
            

        return good_splits 

    # brute force
    # time complexity: O(n^2), inner loop iterates another n times where n is the length of s 
    # space complexity: O(n+n) -> O(n). len(s1)+len(s2) = n, and char dict will carry maximum n elements. 
    def numSplitsBrute(self, s):
        """
        :type s: str
        :rtype: int
        """
        good_splits = 0 
        for i in range(1, len(s)): 
            s1 = s[0:i]
            s2 = s[i:len(s)]
            
            char_dict1 = {}
            num_distinct1 = 0
            num_distinct2 = 0
            
            for j in range(0, len(s1)): 
                if s1[j] not in char_dict1: 
                    char_dict1[s1[j]] = 1
                    num_distinct1 += 1
            char_dict1 = {}
            for j in range(0, len(s2)): 
                if s2[j] not in char_dict1:
                    char_dict1[s2[j]] = 1 
                    num_distinct2 += 1
            
            if num_distinct1 == num_distinct2: 
                good_splits += 1
        
        return good_splits






        # only move one index per iteration, so keep track of whether that distinct count changes or not 
        # add one character to the dict of the first half 
        # remove one character from the dict of the 2nd half 
        # this should cut down a lot of time 