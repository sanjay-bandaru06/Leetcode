class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        c1 = 0 
        c2 = 0
        for i in range(1,n+1):
            if i%m != 0:
                c1 += i
            else:
                c2+=i
        return c1-c2