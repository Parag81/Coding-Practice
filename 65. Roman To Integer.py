"""
Given a string A representing a roman numeral.

Convert A into integer.

A is guaranteed to be within the range from 1 to 3999.

NOTE: Read more 

details about roman numerals at Roman Numeric System




Input Format

The only argument given is string A.
Output Format

Return an integer which is the integer verison of roman numeral string.
For Example

Input 1:
    A = "XIV"
Output 1:
    14

"""


def romanToInt(self, A):
        num = [1, 4, 5, 9, 10, 40, 50, 90,
         100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
                "L", "XC", "C", "CD", "D", "CM", "M"]
        integer = 0
        i = 0
        while i < len(A)-1:
            if A[i]+A[i+1] in sym:
                ind = sym.index(A[i]+A[i+1])
                integer += num[ind]
                i += 2
            else:
                ind = sym.index(A[i])
                integer += num[ind]
                i += 1
        if i != len(A):
            ind = sym.index(A[i])
            integer += num[ind]
        return integer