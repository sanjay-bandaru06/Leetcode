class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        a = 0
        b = 0
        for n in nums:
            if n < 10:
                a += n
            else:
                b += n
        return a != b