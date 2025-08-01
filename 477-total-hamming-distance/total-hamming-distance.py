class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        tot = 0 
        n = len(nums)
        for i in range(32):
            ones = 0
            for num in nums:
                if (num >> i) & 1:
                    ones += 1
            zeros = n - ones  
            tot += ones * zeros
        return tot
