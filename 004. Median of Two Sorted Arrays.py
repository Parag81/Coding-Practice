"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""


def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.nums = nums1 + nums2
        self.nums = sorted(self.nums)
        length = len(self.nums)
        if length%2 == 0:
            i = (length-1)//2
            j = i+1
            median = (self.nums[i]+self.nums[j])/2
            median = float(median)
            return median
        else:
            median = self.nums[(length-1)//2]
            return median
