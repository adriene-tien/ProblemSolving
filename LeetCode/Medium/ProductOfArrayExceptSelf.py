# LeetCode Medium
# Product of Array Except Self Question
# Must be solved in O(n) time and CANNOT use division


class Solution:

    # try with division first and see where that brings me
    # as expected, this doesn't get accepted as a solution by LC due to the use of the division here...
    # but this solution would be O(n) time complexity and O(n) space complexity as len(output) = len(nums)
    def productExceptSelfWithDivision(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_prod = 1
        output = []
        for i in range(0, n):
            total_prod *= nums[i]
        for i in range(0, n):
            output.append(total_prod//nums[i]) # double slash to make sure list is of integers
        return output

    # now try removing the division approach
    # Look up and try a bitwise approach, feels like the only way it can be done
    # time limit still exceeded doing it this way because of while inside for :(
    def productExceptSelfBitwise(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_prod = 1
        output = []
        for i in range(0, n):
            total_prod *= nums[i]

        # total_prod // nums[i]
        for i in range(0, n):

            sign = 1
            if nums[i] * total_prod < 0:
                sign = -1

            mask = 1
            quotient = 0
            local_total_prod = total_prod
            while nums[i] <= local_total_prod:
                nums[i] <<= 1
                mask <<= 1
            while mask > 1:
                nums[i] >>= 1
                mask >>= 1
                if local_total_prod >= nums[i]:
                    local_total_prod -= nums[i]
                    quotient |= mask
            output.append(sign * quotient)

        return output

    # Visualization: Left and Right Sides Product Arrays
    # Although this completes it in O(n), it is still very slow since we need 3 for loops total.
    # O(n) time complexity, O(n) space complexity since it is n + n excluding the output array, 2n -> O(n)
    def productExceptSelfLR(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [None] * n
        right = [None] * n
        output = []

        for i in range(0, n):
            if i == 0:
                left[i] = 1
            else:
                left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                right[i] = 1
            else:
                right[i] = right[i + 1] * nums[i + 1]

        for i in range(0, n):
            output.append(left[i] * right[i])

        return output

    # Try and reduce the for loops needed
    # Operate on one array instead of two (the output array itself), while removing the need for 3 loops
    def productExceptSelf2For(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []

        # initially fills product with what would have been left[] array
        product = 1
        for i in range(0, n):
            output.append(product)
            product = product * nums[i]

        product = 1
        for i in range(n-1, -1, -1):
            output[i] = output[i] * product
            product = product * nums[i]

        return output
