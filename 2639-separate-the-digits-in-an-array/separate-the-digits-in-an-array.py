class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            res.extend([int(d) for d in str(i)])
        return res