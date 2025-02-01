# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, n: int) -> str:
        dic = {
            0 :"",
            1 :"I",
            5 :"V",
            10:"X",
            50:"L",
            100: "C",
            500: "D",
            1000: "M",
        }
        def func(n,s) -> str:
            if n*s in dic.keys():
                return dic[n*s]
            if n <= 3:
                return dic[s] * n
            if n == 4:
                return dic[s] + dic[s*5]
            if n <= 8:
                return dic[s*5] + dic[s] * (n-5)
            if n == 9:
                return dic[s] + dic[s*10]
        res = 0
        s = 1
        string = ""
        while n>0:
            string = func(n%10,s) + string
            n//=10
            s*=10
        return string
            
