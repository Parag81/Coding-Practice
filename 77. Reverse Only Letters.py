"""
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
"""


def reverseOnlyLetters(self, s: str) -> str:
        i, j = 0, len(s) - 1
        lst = [x for x in s]
        while i <= j:
            if lst[i].isalpha() and lst[j].isalpha():
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
            elif lst[i].isalpha():
                j -= 1
            elif lst[j].isalpha():
                i += 1
            else:
                i += 1
                j -= 1
        return "".join(lst)