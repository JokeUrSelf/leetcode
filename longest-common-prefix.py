# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        res = ""
        for i in range(len(strs[0])):
            for x in strs:
                if i >= len(x) or x[i] != strs[0][i]:
                    return res
            res += x[i]
        return res
