"""
Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the longest contiguous segment of 0s in s. Return false otherwise.

For example, in s = "110100010" the longest contiguous segment of 1s has length 2, and the longest contiguous segment of 0s has length 3.
Note that if there are no 0s, then the longest contiguous segment of 0s is considered to have length 0. The same applies if there are no 1s.

 

Example 1:

Input: s = "1101"
Output: true
Explanation:
The longest contiguous segment of 1s has length 2: "1101"
The longest contiguous segment of 0s has length 1: "1101"
The segment of 1s is longer, so return true.
"""

def checkZeroOnes(self, s: str) -> bool:
        max1 = 0
        max0 = 0
        total = 0
        for i in s:
            if i == "0":
                total += 1
                max0 = max(total, max0)
            else:
                total = 0
        total = 0
        for j in s:
            if j == "1":
                total += 1
                max1 = max(total, max1)
            else:
                total = 0
        if max1 > max0:
            return True
        else:
            return False
