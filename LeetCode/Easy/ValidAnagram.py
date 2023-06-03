class Solution:
    def isAnagram_brute(self, s: str, t: str) -> bool:
        # immediate soln: count occurrences of letters in one string and compare to next
        # O(n) time where n is length of the word, s and t are the same length
        # O(n) space

        # return Counter(s) == Counter(t) is a one line solution

        if len(s) != len(t): 
            return False 

        s_letter_count = {}
        for letter in s:
            s_letter_count[letter] = s_letter_count.get(letter, 0) + 1

        for letter in t: 
            if letter in s_letter_count and s_letter_count[letter] > 0: 
                s_letter_count[letter] -=1 
            else: 
                return False

        return True
    
    def isAnagram(self, s: str, t: str) -> bool: 
        # can reduce space usage. since we only care about returning true or false, we can simply compare SORTED order 
        # good sorting algorithms: O(nlogn)
        # space complexity can optimistically be O(1) depending on libraries
        return sorted(s) == sorted(t)
