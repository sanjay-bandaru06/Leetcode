class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # for i in bits:
        #     if bits[i] % 2 == 0:
        #         return True
        # return False
        
        i = 0
        n = len(bits)

        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == n - 1