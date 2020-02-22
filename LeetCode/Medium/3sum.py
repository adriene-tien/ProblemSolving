# LeetCode Medium
# 3Sum Question

class Solution:

    # initial brute force attempt, too slow (checking if the list exists in returnList brings it to O(n^3))
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        returnList = []
        for i in range(0, n):
            startNumber = nums[i]
            subList = [startNumber]
            int_dict = {}
            for j in range(i + 1, n):
                if -(startNumber + nums[j]) in int_dict:
                    subList.append(nums[j])
                    subList.append(-(startNumber + nums[j]))
                    subList.sort()
                    if subList not in returnList:
                        returnList.append(subList)
                    subList = [startNumber]
                else:
                    int_dict[nums[j]] = 1
        return

    # OPTIMIZED:
    # O(n^2) time complexity: outer for loop, and inner while loop ends up touching every element again as well
    # O(1) space complexity since we don't need any extra space, returnList 2d array is part of the question
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:               # no way to have any triplet results, so return an empty list
            return []
        nums.sort()
        returnList = []

        for i in range(0, n):
            if nums[i] > 0:     # this means the entirety of nums is positive, no way to achieve a sum of 0
                break
            if i > 0 and nums[i] == nums[i-1]:  # avoid duplicates
                continue
            l = i+1
            r = n-1
            while l < r:
                total = nums[i]+nums[l]+nums[r]
                if total == 0:
                    returnList.append([nums[i], nums[l], nums[r]])  # appending in this order guarantees ascending
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r += 1
                    l += 1
                    r -= 1
                elif total < 0:
                    # shift our left pointer up and see if the larger number gives us a 0 value now
                    l += 1
                else: # total > 0
                    r -= 1

        return returnList


