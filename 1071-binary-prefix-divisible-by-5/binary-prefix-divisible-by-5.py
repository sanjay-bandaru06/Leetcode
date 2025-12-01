class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        val = 0
        
        for bit in nums:
            val = (val * 2 + bit) % 5
            res.append(val == 0)
        
        return res
