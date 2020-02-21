# LeetCode Easy
# Valid Parentheses Question
# O(n) time complexity
# O(n) space complexity as we use trackStack. Worst case for space is that every character is a left bracket
# so trackStack is fully populated with all characters of s, but is still able to return false at the end

class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return True

        rightBrackets = ["}", "]", ")"]

        if s[0] in rightBrackets:
            return False

        leftBrackets = ["{", "[", "("]
        trackStack = [s[0]]

        for i in range(1, n):
            if len(trackStack) == 0 and s[i] in rightBrackets:
                return False

            if s[i] in leftBrackets:
                trackStack.append(s[i])
            elif s[i] == "}" and trackStack[-1] == "{":
                trackStack.pop()
            elif s[i] == "]" and trackStack[-1] == "[":
                trackStack.pop()
            elif s[i] == ")" and trackStack[-1] == "(":
                trackStack.pop()
            else:
                return False

        if len(trackStack) == 0:
            return True



