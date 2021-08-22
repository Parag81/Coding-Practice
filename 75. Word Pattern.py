"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
"""


def wordPattern(self, pattern: str, s: str) -> bool:
        dict1 = {}
        new = s.split()
        if len(pattern) != len(new):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dict1.keys():
                if new[i] not in dict1.values():
                    dict1[pattern[i]] = new[i]
                else:
                    return False
            else:
                if dict1[pattern[i]] != new[i]:
                    return False
        return True