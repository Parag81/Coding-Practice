"""
Given two integer arrays of equal length target and arr.

In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.

Return True if you can make arr equal to target, or False otherwise.

 

Example 1:

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
"""

"""   Using Hash Tables

def canBeEqual(self, target, arr):
        dict1 = {}
        dict2 = {}
        for ele in target:
            if ele not in dict1:
                dict1[ele] = 1
            else:
                dict1[ele] += 1
        for ele in arr:
            if ele not in dict2:
                dict2[ele] = 1
            else:
                dict2[ele] += 1
        for ele in dict1:
            if ele not in dict2:
                return False
            elif dict1[ele] != dict2[ele]:
                return False
        return True
"""

def canBeEqual(self, target, arr):
        target.sort()
        arr.sort()
        if arr == target:
            return True
        return False