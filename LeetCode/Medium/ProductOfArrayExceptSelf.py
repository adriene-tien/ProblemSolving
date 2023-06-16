# LeetCode Medium
# Product of Array Except Self Question
# Must be solved in O(n) time and CANNOT use division


class Solution:

    # O(n) time
    # O(n) space since I use a left array, could simplify and use only the output array to make it O(1) space since 
    # sometimes we don't count the return array as extra space
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [None]*n
        ret = [None]*n

        # focus on populating the left and right product arrays first 
        # left array first
        left_product = 1
        for i in range(n): 
            if i == 0: 
                left[i] = 1
            else: 
                left_product *= nums[i-1]
                left[i] = left_product
        
        right_product = 1
        for i in reversed(range(n)): 
            if i == n-1:
                ret[i] = left[i]
            else: 
                right_product *= nums[i+1]
                ret[i] = left[i]*right_product
        
        return ret