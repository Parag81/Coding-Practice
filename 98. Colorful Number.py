"""
For Given Number N find if its COLORFUL number or not

Return 0/1

COLORFUL number:

A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
"""


def colorful(self, A):
        A = str(A)
        lst = []
        new = []
        i, j = 0, 0
        k = 0
        n = ""
        while n != A:
            i = 0
            j = k
            while j < len(A):
                n = A[i:j+1]
                lst.append(n)
                i += 1
                j += 1
            k += 1
        for ele in lst:
            mul = 1
            for e in ele:
                mul = mul * int(e)
            new.append(mul)

        if len(new) == len(set(new)):
            return 1
        return 0