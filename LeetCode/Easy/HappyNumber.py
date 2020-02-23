# LeetCode Easy
# Happy Number Question: sum of the square of a number's digits eventually results in 1

class Solution:
    def isHappy(self, n: int) -> bool:
        newNum = n
        if newNum == 1:
            return True
        intDict = {}
        while True:
            if newNum in intDict:
                return False
            else:
                total = 0
                intDict[newNum] = 1
                stringNum = str(newNum)
                for i in range(0, len(stringNum)):
                    squaredNum = pow(int(stringNum[i]), 2)
                    total += squaredNum
                if total == 1:
                    return True
                newNum = total
