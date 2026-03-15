class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set(nums)
        
        for num in nums:
            rev = int(str(num)[::-1])
            s.add(rev)

        return len(s)