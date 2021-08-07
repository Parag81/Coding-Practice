"""
Given a string A and integer B, remove all consecutive same characters that have length exactly B.



Problem Constraints
1 <= |A| <= 100000

1 <= B <= |A|



Input Format
First Argument is string A.

Second argument is integer B.



Output Format
Return a string after doing the removals.
"""


def solve(self, A, B):
        i, j = 0, 0
        new = [x for x in A]
        while j < len(new):
            if new[i] == new[j]:
                j += 1
            else:
                if j-i == B:
                    count = B
                    while count:
                        new.remove(new[i])
                        count -= 1
                    j = i
                else:
                    i = j
        if j - i == B:
            count = B
            while count:
                new.remove(new[i])
                count -= 1
        return "".join(new)