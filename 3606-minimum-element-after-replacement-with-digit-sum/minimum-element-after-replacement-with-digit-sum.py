class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(int(d) for d in str(x)) for x in nums)