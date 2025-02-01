# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        numbersMap = {
            "1" : 1,
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9,
            "0" : 0,
        }
        s = s.strip()
        if s == "": return 0
        isNegative = s[0] == "-"
        if s[0] in "+-": s = s[1:]
        result = 0
        for x in s:
            if x not in numbersMap: break
            result *= 10
            result += numbersMap[x]
        result = -result if isNegative else result
        result = -2147483648 if result < -2147483648 else result
        result = 2147483647 if result > 2147483647 else result
        return result
