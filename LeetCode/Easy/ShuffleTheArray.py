# LeetCode Easy
# Shuffle The Array Question
# O(n/2) -> O(n) time, O(1) space as the array we pass into extend will always be constant size of 2 elements

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ret = []
        for i in range(0, n):
            ret.extend([nums[i], nums[i+n]])
        return ret