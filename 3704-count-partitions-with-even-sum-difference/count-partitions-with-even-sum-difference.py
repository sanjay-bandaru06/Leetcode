class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        new = []
        ans = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            new.append(nums[i])

            left_sum = sum(new)
            right_sum = total - left_sum
            p = left_sum - right_sum

            if p % 2 == 0:
                ans += 1

        return ans

            