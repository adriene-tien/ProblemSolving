# LeetCode Easy
# Arrange Coins Question: July LC Challenge Day 1
# O(1) time, O(1) space
import math

class Solution:

    # Since this involves checking the sum 1+2+3+..+k, I looked to see if I can make use of the sum of series formula
    # sum of 1+2+3+..+k = k(k+1)/2. So in the end I am looking for an integer k to satisfy the equation:
    # k(k+1)/2 <= n
    # k^2 + k <= 2n
    # k^2 + k - 2n <= 0
    # Use quadratic formula here: (-1 +- √(1^2 - 4(1)(-2n)))/2
    # => k = (-1 +- √(1+8n))/2
    # => k = (-1 + √(1+8n))/2, we can take the positive only since k will never be negative (and ofc we know n is positive)
    def arrangeCoins(self, n: int) -> int:
        return math.floor((-1+math.sqrt(1+8*n))/2)


    # My initial brute force solution
    # O(n) time, O(1) space
    def arrangeCoins2(self, n: int) -> int:
        rowCount = 0
        while n - rowCount > 0:
            rowCount += 1
            n = n - rowCount
        return rowCount
