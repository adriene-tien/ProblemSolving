class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # use two pointer approach requires sorting the array first 
        # O(nlogn) time, still O(1) space
        nums.sort()
        low = 0 
        high = len(nums)-1
        maxSum = -1
        while low != high: 
            currentSum = nums[low]+nums[high]
            if currentSum < k:
                low += 1 
                if currentSum > maxSum: 
                    maxSum = currentSum
            else:
                high -= 1 
            
            
        return maxSum 
        
        
        
        # O(n^2) brute force solution
        # check = {}
        # maxSum = -1
        # for i in range(len(nums)): 
        #     for j in range(i+1, len(nums)): 
        #         currentSum = nums[i]+nums[j]
        #         if currentSum < k and currentSum > maxSum: 
        #             maxSum = currentSum 
        # return maxSum 