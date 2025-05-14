class Solution:
    def minimumSum(self, num: int) -> int:
        k = sorted(str(num))
        return int(k[0] + k[3]) + int(k[1]+k[2])