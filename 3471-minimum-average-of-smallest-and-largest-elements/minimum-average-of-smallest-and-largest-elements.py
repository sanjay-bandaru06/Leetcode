class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        minavg = float('inf')

        for i in range(n // 2):
            avg = (nums[i] + nums[n - 1 - i]) / 2
            minavg = min(minavg, avg)
        
        return minavg