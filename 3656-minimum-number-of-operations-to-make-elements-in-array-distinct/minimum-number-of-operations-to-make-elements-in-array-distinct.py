class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        oper = 0
        while len(nums) != len(set(nums)):
            nums = nums[3:] 
            oper += 1
        return oper