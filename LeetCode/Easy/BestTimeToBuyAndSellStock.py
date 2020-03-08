# LeetCode Easy
# Best Time to Buy And Sell Stock Question
# Time complexity: O(n), one pass through the prices array
# Space complexity: O(1)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find the minimum and the next maximum
        n = len(prices)
        minimum = float("inf")
        maxProfit = 0
        for i in range(0, n):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                if prices[i] - minimum > maxProfit:
                    maxProfit = prices[i] - minimum

        return maxProfit
