"""
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

 

Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
"""

def canMakeArithmeticProgression(self, arr):
        arr.sort()
        if len(arr) == 2: return True
        diff = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != diff:
                return False
        return True
