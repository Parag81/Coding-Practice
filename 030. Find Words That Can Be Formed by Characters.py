"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
"""

def countCharacters(self, words, chars):
        total = 0
        present = False
        for s in words:
            if len(s) > len(chars):
                continue
            for ch in s:
                if ch not in chars:
                    present = False
                    break
                else:
                    present = True
                    if s.count(ch) > chars.count(ch):
                        present = False
                        break
            if present:
                total += len(s)
        return total
