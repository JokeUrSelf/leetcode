// https://leetcode.com/problems/roman-to-integer/

public class Solution {
    public int RomanToInt(string s)
    {
        var d = new Dictionary<char,int>{
            {'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}
        };
        int sum = 0;
        for (int i = s.Length -2; i >= 0; i--)
            sum = d[s[i]] < d[s[i+1]] ? sum - d[s[i]] : sum + d[s[i]];
        return sum + d[s[s.Length - 1]];
    }
}
