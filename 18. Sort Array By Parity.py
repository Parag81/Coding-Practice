"""
Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by all the odd elements of nums.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

"""

def sortArrayByParity(self, nums):
        lst1 = []
        lst2 = []
        for i in nums:
            if i % 2 == 0:
                lst1.append(i)
            else:
                lst2.append(i)
        main = []
        main = lst1 + lst2
        return main