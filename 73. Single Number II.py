"""
Given a non-empty array of integers nums, every element appears thrice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

def singleNumber(self, nums):
        nums.sort()
        i,j = 0,0
        count = 0
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
                count += 1
            else:
                if count != 3:
                    return nums[i]
                else:
                    i = j
                    count = 0
        if count != 3:
            return nums[i]