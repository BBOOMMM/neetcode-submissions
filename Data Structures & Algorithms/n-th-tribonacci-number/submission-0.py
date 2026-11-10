class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        if n==0:
            return a
        elif n==1:
            return b
        elif n==2: 
            return c
        else:
            while n>=3:
                a, b, c = b, c, a+b+c
                n -= 1
            return c