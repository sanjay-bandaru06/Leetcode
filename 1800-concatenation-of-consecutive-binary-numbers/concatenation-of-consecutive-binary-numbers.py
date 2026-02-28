class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 1000000007
        res = 0
        
        for i in range(1, n + 1):
            bits = i.bit_length()
            res = ((res << bits) + i) % mod
        
        return res