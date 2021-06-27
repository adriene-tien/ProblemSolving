class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer approach. This is better space wise O(1) and still O(n) time. 
        low = 0
        high = len(numbers)-1
        while low != high: 
            if numbers[low]+numbers[high] < target: 
                low += 1 
            elif numbers[low]+numbers[high] > target: 
                high -=1
            else: 
                return [low+1, high+1]
        
        
        # O(n) time, O(n) space. hash table approach 
        # check = {}
        # for i in range(len(numbers)): 
        #     if target-numbers[i] not in check: 
        #         check[numbers[i]] = i+1
        #     else: 
        #         return [check[target-numbers[i]], i+1]