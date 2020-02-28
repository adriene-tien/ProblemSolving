# LeetCode Easy
# Merge Sorted Array Question: Modify nums1 in place, don't return anything (nums1 has enough space for nums2 elements)
# Time complexity is O(nlogn + n) and for large inputs nlogn is dominant therefore TC: O(nlog(n))
# Space complexity is O(1), don't use any extra space. we just work with the given nums1 and nums2.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if len(nums1) == 0 or len(nums2) == 0:  # then there is nothing to change
            return

        # O(n)
        for i in range(0, n):
            nums1[i + m] = nums2[i]

        # O(nlog(n))
        nums1.sort()

