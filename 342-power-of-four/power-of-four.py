class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if (n==0): 
            return False;
        if (n & n-1 == 0 and (n-1) % 3 == 0):
            return True
        else:
            return False
        