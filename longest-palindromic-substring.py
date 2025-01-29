# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def safe_s(i:int):
            if i>=len(s) or i<0:
                return i
            return s[i]

        def func(l, r):
            if safe_s(l) != safe_s(r):
                return l+1, r-1
            return func(l - 1, r + 1)

        max_str = ""
        i = 0
        while i < len(s):
            init = i
            while s[i] == safe_s(i+1):
                i += 1
            i+=1
            tmp = func(init - 1, i)
            if len(max_str) < tmp[1]-tmp[0]+1:
                max_str = s[tmp[0]:tmp[1]+1]
        return max_str
  
