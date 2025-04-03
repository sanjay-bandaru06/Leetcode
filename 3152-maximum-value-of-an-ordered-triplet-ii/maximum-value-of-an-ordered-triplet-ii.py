class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # max_value = 0
        # n = len(nums)

        # if n<3:
        #     return 0
        
        # for i in range(n - 2):
        #     for j in range(i + 1, n - 1):
        #         max_k = max(nums[j + 1:])
        #         max_value = max(max_value, (nums[i] - nums[j]) * max_k)
                    
        # return max_value
        n = len(nums)
        if n < 3:
            return 0

        # Compute max_suffix
        max_suffix = [0] * n
        max_suffix[n - 1] = nums[n - 1]

        for k in range(n - 2, -1, -1):
            max_suffix[k] = max(max_suffix[k + 1], nums[k])

        # Compute result with prefix tracking
        max_prefix = nums[0]
        max_value = 0

        for j in range(1, n - 1):
            max_prefix = max(max_prefix, nums[j - 1])
            max_value = max(max_value, (max_prefix - nums[j]) * max_suffix[j + 1])

        return max_value