# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0): return False

        reversed = 0;
        i = x
        while i > 0:
            reversed = reversed * 10 + i % 10
            i //= 10
        if reversed == x:
            return True
        return False
