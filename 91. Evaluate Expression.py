"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.




Input Format

The only argument given is character array A.
Output Format

Return the value of arithmetic expression formed using reverse Polish Notation.
For Example

Input 1:
    A =   ["2", "1", "+", "3", "*"]
Output 1:
    9
Explaination 1:
    starting from backside:
    *: ( )*( )
    3: ()*(3)
    +: ( () + () )*(3)
    1: ( () + (1) )*(3)
    2: ( (2) + (1) )*(3)
    ((2)+(1))*(3) = 9
"""


def evalRPN(self, A):
        operand = []
        for ele in A:
            if ele not in ('+', '-', '*', '/'):
                operand.append(ele)
            else:
                a = operand.pop()
                b = operand.pop()
                v = str(b)+ele+str(a)
                v = eval(v)
                operand.append(v)
        return operand[0]