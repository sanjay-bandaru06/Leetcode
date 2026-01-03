class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        t = 0
        for i in range (len(nums)):
            if i % 2 == 0:
                t += nums[i]
            else:
                t -= nums[i]
        return t
        