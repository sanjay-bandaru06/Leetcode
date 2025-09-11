class Solution:
    def numberOfMatches(self, n: int) -> int:
        t = 0 

        while n>1:
            if n % 2 == 0:
                m =  n // 2
                n = n // 2
            else:
                m = (n-1) // 2
                n = (n-1) // 2+1

            t += m
            
        return t
            