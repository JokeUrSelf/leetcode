# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n3 = sorted(nums1 + nums2)
        N = len(n3)
        x = (N-1)//2
        return n3[x] if N % 2 else (n3[x] + n3[x+1])/2
