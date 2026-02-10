class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n= len(nums)
        ans = 0

        for i in range(n):
            ev_set = set()
            od_set = set()

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    ev_set.add(nums[j])
                else:
                    od_set.add(nums[j])

                if len(ev_set) == len(od_set):
                    ans = max(ans, j-i+1)
        return ans