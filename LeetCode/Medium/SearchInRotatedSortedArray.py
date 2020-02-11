# LeetCode Medium
# Search In Rotated Sorted Array Question
# O(log(n)) time complexity, as dictated by the question.
# O(1) space complexity, constant number of variables being used, nothing depending on size of input
# Seeing this time complexity requirement hints hard at the required use of binary search

class Solution:

    # e.g. [4, 5, 6, 7, 0, 1, 2]
    # build off my solution in FindMinRotatedSortedArray. approach can be splitting array into two based on min element
    def search(self, nums: List[int], target: int) -> int:

        # generic binary search when we get to the point where we can split the array
        def searchForTargetWithRotation(minIndex, maxIndex):
            while minIndex <= maxIndex:
                guessIndex = (minIndex + maxIndex) // 2
                if nums[guessIndex] == target:
                    return guessIndex
                else:
                    if nums[guessIndex] < target:
                        minIndex = guessIndex + 1
                    else:  # nums[guessIndex] > target
                        maxIndex = guessIndex - 1
            return -1

        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1

        minIndex = 0
        maxIndex = n - 1
        minElementIndex = -1
        if nums[minIndex] < nums[maxIndex]:
            minElementIndex = 0

        # find minimum element first, point of rotation
        if minElementIndex == -1:
            while minIndex <= maxIndex:
                guessIndex = (minIndex + maxIndex) // 2
                if nums[guessIndex] > nums[guessIndex + 1]:
                    minElementIndex = guessIndex + 1
                    break
                elif nums[guessIndex] > nums[maxIndex]:
                    minIndex = guessIndex
                else:
                    maxIndex = guessIndex

        if nums[minElementIndex] == target:
            return minElementIndex

        # now have minimum element, conduct binary search on whichever side of array depending on target
        if minElementIndex == 0:  # not rotated at some intermediate part of the array, search entire
            return searchForTargetWithRotation(0, n - 1)
        elif target < nums[0]:
            return searchForTargetWithRotation(minElementIndex, n - 1)
        else:  # target > nums[0]
            return searchForTargetWithRotation(0, minElementIndex)







