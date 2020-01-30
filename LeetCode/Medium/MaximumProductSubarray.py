# LeetCode Medium
# Maximum Product Array Question
# Negative multiplication -> positive number, changing the question quite significantly from MaximumSubArray (LC Easy)

class Solution:

    # I tried to approach this question in the same way I approached MaximumSubArray (the LC easy, sum instead of prod)
    # Since double negatives bring positive, I knew that I also would want to keep track of the lowest product each time
    # O(n) Time complexity
    # O(1) Space complexity, I use an array/list but it is constant size of 2 no matter the input
    # Currently only faster than 40% of other submissions despite being linear time
    # But better than 100% of others in memory usage
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        maxproduct = nums[0]
        product = [maxproduct, maxproduct]
        for i in range(1, n):
            prod1 = product[1]*nums[i]
            prod0 = product[0]*nums[i]
            product[1] = max(prod1, prod0, nums[i])
            product[0] = min(prod1, prod0, nums[i])
            if product[1] > maxproduct:
                maxproduct = product[1]

        return maxproduct

    # there should be a way to optimize this, attempt further
    def maxProduct2(self, nums: List[int]) -> int:
        pass
