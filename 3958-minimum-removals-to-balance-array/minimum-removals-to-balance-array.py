class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        l = 0
        max_keep = 1 

        for r in range(n):
            while nums[r] > nums[l] * k:
                l += 1

            max_keep = max(max_keep, r - l + 1)

        return n - max_keep