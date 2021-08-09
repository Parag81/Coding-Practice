"""
Given an integer A, convert it to a roman numeral, and return a string corresponding to its roman numeral version
"""


def intToRoman(self, A):
        num = [1, 4, 5, 9, 10, 40, 50, 90,
         100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
                "L", "XC", "C", "CD", "D", "CM", "M"]
        roman = ""
        i = 12
        while A > 0:
            q = A // num[i]
            A = A % num[i]
            while q:
                roman = roman + sym[i]
                q -= 1
            i -= 1
        return roman