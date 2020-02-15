# LeetCode Medium
# Find Minimum Element in Rotated Sorted Array Question

class Solution:

    # Given that there are no duplicates, the brute force seems pretty straight forward
    # O(n) time complexity, O(1) space complexity (no extra space needed)
    def findMinBF(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i] < nums[0]:
                return nums[i]

        return nums[0]

    # linear solution will be slow if e.g. last item is the minimum element
    # don't want to iterate one by one - optimize via binary search: work for sorted arrays
    # min() will only ever compare 3 terms so this would run in constant time.
    # O(log(n)) time complexity, O(1) space complexity
    # clean and try without min()?
    # currently, best case seems to run faster than 96% of other submissions, pretty decent
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        minBound = 0
        maxBound = n - 1
        if minBound == maxBound:
            return nums[0]
        minElement = nums[0]
        while (maxBound - minBound > 1):
            indexCheck = (maxBound + minBound) // 2
            if nums[indexCheck] < nums[0]:
                maxBound = indexCheck
                if nums[indexCheck] < minElement:
                    minElement = nums[indexCheck]
            else:
                minBound = indexCheck
        return min(minElement, nums[minBound], nums[maxBound])

    # avoid using min() function. follow off of search in rotated sorted array simpler solution for finding min elem
    def findMin2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        minIndex = 0
        maxIndex = n - 1

        if nums[minIndex] < nums[maxIndex]:
            return nums[minIndex]

        while minIndex <= maxIndex:
            guessIndex = (minIndex + maxIndex) // 2
            if nums[guessIndex] > nums[guessIndex + 1]:
                return nums[guessIndex + 1]
            elif nums[guessIndex] > nums[0]:
                minIndex = guessIndex
            else:
                maxIndex = guessIndex

