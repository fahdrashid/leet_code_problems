class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        for i in range(len(s)):
            if (s[i] == "V" or s[i] =="X") and (s[i-1] == "I") and i != 0:
                number -= 2
            elif (s[i] == "L" or s[i] =="C") and (s[i-1] == "X") and i != 0:
                number -= 20
            elif (s[i] == "D" or s[i] =="M") and (s[i-1] == "C") and i != 0:
                number -= 200
            number += roman[s[i]]
        return number