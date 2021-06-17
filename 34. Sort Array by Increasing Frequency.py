"""
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
"""

def frequencySort(self, nums):
        output = []
        dict1 = {}
        fre = []        
        for ele in nums:
            if ele not in dict1:
                dict1[ele] = 1
            else:
                dict1[ele] += 1
        for ele in dict1:
            if dict1[ele] not in fre:
                fre.append(dict1[ele])
        fre.sort()
        for e in fre:
            new = []
            for ele in dict1:
                if dict1[ele] == e:
                    new.append(ele)
            new.sort(reverse=True)
            for i in new:
                for _ in range(dict1[i]):
                    output.append(i)
        return output