"""
Given four positive integers A, B, C, D, determine if there’s a rectangle such that the lengths of its sides are A, B, C and D (in any order).

If any such rectangle exist return 1 else return 0.



Problem Constraints
1 <= A, B, C, D <= 100



Input Format
First argument is an interger A.

Second argument is an interger B.

Third argument is an interger C.

Fourth argument is an interger D.



Output Format
If any such rectangle exist whose sides are A, B, C, D in any orde then return 1 else return 0.
"""


def solve(self, A, B, C, D):
        lst = [A, B, C, D]
        table = {}
        for l in lst:
            if l not in table:
                table[l] = 1
            else:
                table[l] += 1
        if len(table) == 2:
            for val in table:
                if table[val] != 2:
                    return 0
            return 1
        return 0