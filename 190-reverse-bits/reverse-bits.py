class Solution:
    def reverseBits(self, n: int) -> int:
        bits = format(n, '032b')
        reversed = bits[::-1]  
        res = int(reversed, 2)
        return res
        
        