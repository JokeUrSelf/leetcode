# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution:
    def countOdds(self, l: int, h: int) -> int:
        return (h - l + 1 + (h % 2 and l % 2)) // 2
