# LeetCode Easy 
# Verifying An Alien Dictionary Question 

# Time complexity: 
# let m = len(order), n = len(words), j = max(len(words[i])) 
# O(m+n*j) I think 
# Space complexity: O(m) due to alphabetDict 
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabetDict = {}
        for i in range(0, len(order)): 
            alphabetDict[order[i]] = i
        for i in range(1, len(words)):
            caught = 0 
            if words[i] != words[i-1]:
                iterRange = min(len(words[i]), len(words[i-1]))
                for j in range(0, iterRange): 
                    currWordCharPos = alphabetDict[words[i][j]]
                    prevWordCharPos = alphabetDict[words[i-1][j]]
                    if currWordCharPos < prevWordCharPos: 
                        return False 
                    elif currWordCharPos > prevWordCharPos: 
                        caught = 1 
                        break
                if (len(words[i]) < len(words[i-1])) and caught == 0:
                    return False 
        
        return True      