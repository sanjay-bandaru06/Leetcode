class Solution:
    def hasSameDigits(self, s: str) -> bool:
        nums = [int(x) for x in s]

        while len(nums) > 2:
            temp = []
            for i in range(len(nums) - 1):
                temp.append((nums[i] + nums[i + 1]) % 10)
            nums = temp

        return nums[0] == nums[1]