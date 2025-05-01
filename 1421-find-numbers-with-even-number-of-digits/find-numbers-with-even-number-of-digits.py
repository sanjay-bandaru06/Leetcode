class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            # if len(str(i)) % 2 == 0:
            k = int(math.log10(i)) + 1
            if k % 2 == 0:
                count += 1
        return count
                