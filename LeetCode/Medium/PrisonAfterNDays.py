# LeetCode Medium
# Prison After N Days Question: July LC Chal Day 3
# O(1) time, O(1) space


class Solution:

    # Need to figure out an optimized version once N hits very high: work with the 6 cells only
    # Understand that since there are only 6 cells, there are max 2^6 = 64 patterns where not all of these are valid
    # So if N > 64, then at some point we will end up hitting a cycle
    # I want to use a dict to keep track of patterns that have already been hit, to jump i forward in the loop,
    # skipping all redundant cycle loops
    # O(1) time complexity as the max cycle length will be however many valid patterns there are out of the 64 (which
    # does not grow with input size), and O(1) space as prevPattern length is max 8, and there are again a limited
    # number of patterns that we will be inserting into the dictionary. It does not matter how big N is
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        m = len(cells)
        lastFound = {}
        checkCycle = 0
        prevPattern = ''.join(str(elem) for elem in cells)
        i = 0
        while i < N:
            newPattern = ''
            for j in range(1, m - 1):
                if (prevPattern[j - 1] == "1" and prevPattern[j + 1] == "1") or (
                        prevPattern[j - 1] == "0" and prevPattern[j + 1] == "0"):
                    newPattern += "1"
                else:
                    newPattern += "0"
            newPattern = "0" + newPattern + "0"

            if newPattern in lastFound and checkCycle == 0:
                if N % (i - lastFound[newPattern]) == 0:
                    break
                else:
                    i = N - (N % (i - lastFound[newPattern]))
                checkCycle = 1

            lastFound[newPattern] = i
            prevPattern = newPattern
            i += 1

        ret = []
        for i in range(0, len(prevPattern)):
            ret.append(prevPattern[i])
        return ret


        # Brute force solution (too slow since N can reach 10^9)
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