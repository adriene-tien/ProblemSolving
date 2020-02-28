# LeetCode Easy
# Happy Number Question: sum of the square of a number's digits eventually results in 1
# Time complexity: # of digits of a number is given by log(n) so TC: O(log(n)).
# Each subsequent number we process ends up being added log(log(n)), log(log(log(n))), etc. terms where n = original num
# log(n) term is dominant for large inputs so this ends up being our overall time complexity


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
