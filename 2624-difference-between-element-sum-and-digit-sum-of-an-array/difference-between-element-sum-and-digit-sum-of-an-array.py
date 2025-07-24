class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        tot = 0
        s = sum(nums)
        for i in nums:
            for digit in str(i):  
                tot += int(digit)
        return s - tot