# Daily Coding Problem #273 - Easy
# Description
# A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements,
# return a fixed point, if one exists. Otherwise, return False.


class Solution:

    # takes an array `nums`, returns integer of a fixed point, otherwise a bool
    # given the array is sorted, this hints at a binary search approach to improve time from a linear search
    # O(log(n)) time complexity
    # O(1) space complexity: only use minIndex, maxIndex, repeatCheck
    def fixedPointSearch(self, nums):
        n = len(nums)
        if n == 0:
            return False
        elif n == 1:
            return 0 if nums[0] == 0 else False
        minIndex = 0
        maxIndex = n-1
        repeatCheck = False

        while minIndex <= maxIndex:
            if nums[minIndex] == minIndex:
                return minIndex
            if nums[maxIndex] == maxIndex:
                return maxIndex

            if maxIndex - minIndex == 1 and not repeatCheck:
                repeatCheck = True
            if repeatCheck:
                break
            guessIndex = (minIndex + maxIndex)//2
            if nums[guessIndex] == guessIndex:
                return guessIndex
            elif nums[guessIndex] > guessIndex:
                maxIndex = guessIndex
            else: # nums[guessIndex] < guessIndex:
                minIndex = guessIndex

        return False


# testing inputs
# test even and odd sized arrays, no fixed point, single element. arrays of size 2, 3 +

# expected output: 2
# actual output: 2
nums1 = [-2, -1, 2, 5, 9]
test1 = Solution()
print(test1.fixedPointSearch(nums1))

# expected output: False
# actual output: False
nums2 = [-1, 0, 1, 2, 3, 4]
test2 = Solution()
print(test2.fixedPointSearch(nums2))

# expected output: 0
# actual output: 0
nums3 = [0]
test3 = Solution()
print(test2.fixedPointSearch(nums3))

# expected output: False
# actual output: False
nums4 = [1]
test4 = Solution()
print(test4.fixedPointSearch(nums4))

# expected output: False
# actual output: False
nums5 = [1, 2]
test5 = Solution()
print(test5.fixedPointSearch(nums5))

# expected output: 2
# actual output: 2
nums6 = [-5, 0, 2]
test6 = Solution()
print(test6.fixedPointSearch(nums6))

# expected output: 0
# actual output: 0
nums7 = [0, 1, 2, 3, 4, 5]
test7 = Solution()
print(test7.fixedPointSearch(nums7))

# expected output: 3
# actual output: 3
nums8 = [-2, -1, 0, 3, 5, 9]
test8 = Solution()
print(test8.fixedPointSearch(nums8))

# expected output: 7
# actual output:
nums9 = [-10, -2, -1, 0, 1, 2, 3, 7]
test9 = Solution()
print(test9.fixedPointSearch(nums9))



