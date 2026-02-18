class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # b = bin(n)[2:]  
        # for i in range(len(b) - 1):
        #     if b[i] == b[i + 1]:
        #         return False
        # return True

        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0