# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for x in nums:
            if x > nums[i]:
                i += 1
                nums[i] = x
        return i + 1
