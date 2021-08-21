"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
"""


def containsDuplicate(self, nums: List[int]) -> bool:
        dict1 = {}
        for ele in nums:
            if ele in dict1:
                dict1[ele] += 1
            else:
                dict1[ele] = 1
        for ele in dict1:
            if dict1[ele] > 1:
                return True
        return False