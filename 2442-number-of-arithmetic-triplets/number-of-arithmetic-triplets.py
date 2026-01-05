class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        s = set(nums)

        for x in nums:
            if x + diff in s and x + 2*diff in s:
                count += 1

        return count