class Solution:
    def maxProduct(self, n: int) -> int:
        dig = [int(d) for d in str(n)] 
        dig.sort()
        return dig[-1] * dig[-2]
    