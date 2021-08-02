"""
Given an integer A you need to find the Ath fibonacci number modulo 109 + 7.

The first fibonacci number F1 = 1

The first fibonacci number F2 = 1

The nth fibonacci number Fn = Fn-1 + Fn-2 (n > 2)



Problem Constraints
1 <= A <= 109.



Input Format
First argument is an integer A.



Output Format
Return a single integer denoting Ath fibonacci number modulo 10^9 + 7.
"""


d={}
def fibi(n):
    if(n==0):
        return 0
    elif(n==1 or n==2):
        return 1
    elif(n==4):
        return 3
    if(n in d):
        return d[n]
    elif(n%2!=0):
        d[n]=(fibi(n//2)**2 + fibi(n//2+1)**2)%(10**9+7)
        return d[n]
    else:
        d[n]=(2*fibi(n//2)**2 + fibi(n//2-3)*fibi(n//2))%(10**9+7)
        return d[n]