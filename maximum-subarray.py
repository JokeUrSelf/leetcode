# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, n) -> int:
        result = 0
        maxim = -sys.maxsize
        for i in range(len(n)):
            result+=n[i];
            if n[i] > result:
                result = n[i]
            if result > maxim:
                maxim = result
        return maxim
