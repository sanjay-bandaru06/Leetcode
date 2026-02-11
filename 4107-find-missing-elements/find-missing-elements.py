class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        small = min(nums)
        large = max(nums)
        
        nums_set = set(nums)
        res = []
        
        for i in range(small, large + 1):
            if i not in nums_set:
                res.append(i)
        
        return res