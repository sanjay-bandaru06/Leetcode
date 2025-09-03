class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        u = list(set(nums))
        u.sort(key=lambda x: nums.count(x), reverse=True)
        return u[:k]