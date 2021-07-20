class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9: 
            digits[-1] += 1 
            return digits 
        else: 
            # need to consider carry case. the return array is potentially one element bigger than digits 
            i = len(digits)-1
            while True: 
                digits[i] = 0 
                if i != 0 and digits[i-1] == 9: 
                    i -= 1  
                elif i == 0: 
                    digits.insert(0, 1)
                    return digits
                else: 
                    digits[i-1] += 1 
                    return digits 

# O(n) time, O(1) space 