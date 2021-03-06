"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
"""

def minimumAbsDifference(self, arr):
        output = []
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(1, len(arr)-1):
            if arr[i+1] - arr[i] < diff:
                diff = arr[i+1] - arr[i]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == diff:
                output.append([arr[i], arr[i+1]])
        return output