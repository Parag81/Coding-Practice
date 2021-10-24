"""
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
"""


def sortArrayByParityII(self, nums):
        even = []
        odd = []
        for ele in nums:
            if ele % 2 == 0:
                even.append(ele)
            else:
                odd.append(ele)
        output = []
        for i in range(len(even)):
            output.append(even[i])
            output.append(odd[i])
        return output
