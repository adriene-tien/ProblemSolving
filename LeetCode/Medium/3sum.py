# LeetCode Medium
# 3Sum Question

class Solution:

    # initial attempt, too slow (checking if the list exists in returnList brings it to O(n^3)
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


    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()     # sort is O(n*log(n))

        for i in range(0, n):


