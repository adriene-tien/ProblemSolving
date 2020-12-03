# LeetCode Easy 
# Shorted Word Distance Problem 
# word1arr = [1, 4]
# word2arr = [3]
# need to make sure that the comparison is not between a word and itself, but with the other word 

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        shortestDist = len(words)-1
        lastWasWord1 = False
        lastWasWord2 = False
        word1Index = -1
        word2Index = -1
        for i in range(0, len(words)): 
            if words[i] == word1: 
                word1Index = i 
                lastWasWord1 = True
                lastWasWord2 = False
                if word2Index >= 0:
                    dist = word1Index - word2Index 
                    if dist < shortestDist: 
                        shortestDist = dist 
            elif words[i] == word2: 
                word2Index = i
                lastWasWord2 = True 
                lastWasWord1 = False 
                if word1Index >= 0: 
                    dist = word2Index - word1Index
                    if dist < shortestDist: 
                        shortestDist = dist 
        
        return shortestDist