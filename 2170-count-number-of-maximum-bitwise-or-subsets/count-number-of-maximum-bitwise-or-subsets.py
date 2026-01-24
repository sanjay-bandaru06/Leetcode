class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        m = 0
        for n in nums:
            m |= n

        count = 0

        def dfs(i, curr):
            nonlocal count
            if i == len(nums):
                if curr == m:
                    count += 1
                return
            
            dfs(i + 1, curr | nums[i])
            dfs(i + 1, curr)          
        dfs(0, 0)
        return count
        
        