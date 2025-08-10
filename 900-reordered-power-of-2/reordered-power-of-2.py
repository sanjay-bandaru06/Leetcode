class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # if n & n-1 == 0:
        #     return True
        # return False
        target = sorted(str(n))
        for i in range(31):
            if sorted(str(1 << i)) == target:
                return True
        return False