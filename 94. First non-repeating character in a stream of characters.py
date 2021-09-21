"""
Given a string A denoting a stream of lowercase alphabets. You have to make new string B.

B is formed such that we have to find first non-repeating character each time a character is inserted to the stream and append it at the end to B. If no non-repeating character is found then append '#' at the end of B.


Problem Constraints
1 <= length of the string <= 100000


Input Format
The only argument given is string A.


Output Format
Return a string B after processing the stream of lowercase alphabets A.


Example Input
Input 1:

 A = "abadbc"

Example Output
Output 1:

 "aabbdd"

Example Explanation
Explanation 1:

    "a"      -   first non repeating character 'a'
    "ab"     -   first non repeating character 'a'
    "aba"    -   first non repeating character 'b'
    "abad"   -   first non repeating character 'b'
    "abadb"  -   first non repeating character 'd'
    "abadbc" -   first non repeating character 'd'
"""


def solve(self, A):
        s = set()
        stack = []
        result = []

        for i in A:
            if i not in s:
                s.add(i)
                stack.append(i)
                result.append(stack[0])
            else:
                if i in stack:
                    stack.remove(i)
                if stack:
                    result.append(stack[0])
                else:
                    result.append("#")

        return "".join(result)