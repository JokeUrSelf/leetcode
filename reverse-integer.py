# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        z = 1 if x >= 0 else -1
        while z*x > 0:
            result = result*10+x%(10*z)
            x=x//(z*10)*z
        if not(-2**31 <= result <= 2**31 - 1): return 0
        return result
