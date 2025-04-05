class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s = min(nums)
        l = max(nums)
        while l % s != 0:
            s, l = l % s, s

        return s