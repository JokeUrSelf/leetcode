# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i,x in enumerate(nums):
            j = dic.get(target-x)
            if j is not None and j != i:
                return [i,j]
            dic[x]=i
