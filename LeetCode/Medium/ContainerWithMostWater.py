# LeetCode Medium
# Container With Most Water Question
# Time complexity: O(n) as I managed to figure out the one pass solution
# Space complexity: O(1)

def maxArea(self, height: List[int]) -> int:
    n = len(height)  # n is at least 2
    maxWater = 0
    left = 0
    right = n - 1
    while left < right:
        if height[left] < height[right]:
            water = (right - left) * height[left]
            if water > maxWater:
                maxWater = water
            left += 1
        else:
            water = (right - left) * height[right]
            if water > maxWater:
                maxWater = water
            right -= 1

    return maxWater