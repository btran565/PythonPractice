'''class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {"I" : 1, "V" : 5, "X" : 10, 
                    "L" : 50, "C" : 100, "D" : 500, "M" :1000}
        
        ans = 0

        for i in range(len(s)):
            if i +1 < len(s) and roman[s[i]] < roman[s[i+1]]:'''
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = values.get(s[-1])
        for i in reversed(range(len(s) - 1)):
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total
    
#needs to be studied further