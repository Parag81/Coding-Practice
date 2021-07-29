"""
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.
Example Input
Input 1:

[1, 2, 3]


Example Output
Output 1:

[1, 2, 4]


Example Explanation
Explanation 1:

Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.
"""

def plusOne(self, A):
        number = ""
        for ele in A:
            number += str(ele)
        number = int(number) + 1
        ans = []
        for ele in str(number):
            ans.append(int(ele))
        return ans