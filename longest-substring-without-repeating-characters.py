# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        N = len(s) -1
        sub = ""
        i = 0
        fin = 0
        while i < len(s):
            if s[i] not in sub:
                sub += s[i]
                dic[s[i]] = i
            else:
                fin = max(len(sub), fin)
                sub = ""
                i = dic[s[i]]
            i += 1
        fin = max(len(sub), fin)
        return fin
