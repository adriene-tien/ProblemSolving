# LeetCode Medium
# Prison After N Days Question: July LC Chal Day 3


class Solution:

    # Need to figure out an optimized version once N hits very high: work with the 6 cells only
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:



    # Brute force solution (too slow)
    # O(nm) time complexity
    # O(1) space complexity as we only ever need the repeat usage of an array of size 8
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        m = len(cells)
        for i in range(0, N):
            tmpArr = []
            tmpArr.append(0)
            for j in range(1, m-1):
                if (cells[j-1] == 1 and cells[j+1] == 1) or (cells[j-1] == 0 and cells[j+1] == 0):
                    tmpArr.append(1)
                else:
                    tmpArr.append(0)
            tmpArr.append(0)
            cells = tmpArr
        return cells