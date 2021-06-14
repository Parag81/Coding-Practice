"""
Given an array words of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
"""

def commonChars(self, words):
        ele = words[0]
        lst = []
        present = False
        for c in ele:
            for i in range(1, len(words)):
                if c not in words[i]:
                    present = False
                    break
                else:
                    present = True
                    new = words[i].replace(c, '-', 1)
                    words[i] = new
                    if ele.count(c) > words[0].count(c) and words[0].count(c) == 0:
                        present = False
            if present:
                lst.append(c)
        return lst