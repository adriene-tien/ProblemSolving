# LeetCode Medium
# ZigZag Conversion Question
# 


class Solution:

    # need to optimize, try doing the math based on the string itself?
    def convert(self, s: str, numRows: int) -> str:
        # list of a list
        zigzag = []
        for i in range(0, numRows):
            zigzag.append([])

        n = len(s)
        if n == 0:
            return ""

        count = 0
        for i in range(0, n):
            if count < numRows:
                rowToAddTo = count % numRows
                zigzag[rowToAddTo].append(s[i])
            else:
                rowToAddTo = ((count % numRows) + 2)
                zigzag[-rowToAddTo].append(s[i])
            count += 1
            if count > (2 * numRows - 3):
                count = 0

        ret = ""
        for i in range(0, numRows):
            for j in range(0, len(zigzag[i])):
                ret += zigzag[i][j]
        print(zigzag)
        return ret
