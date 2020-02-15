# LeetCode Medium
# 3Sum Question

class Solution:

    # initial solution 
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
        return returnList

