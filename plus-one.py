# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits):
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        for i in range(len(digits) - 1, -1, -1):
            digits[i] = 0

            if not i:
                return [1] + digits
                
            if digits[i - 1] < 9:
                digits[i - 1] += 1
                return digits
