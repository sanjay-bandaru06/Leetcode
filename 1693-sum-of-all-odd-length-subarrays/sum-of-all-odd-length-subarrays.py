class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        t = 0
        for i in range(len(arr)):
            total_sub = (i + 1) * (len(arr) - i)
            odd = (total_sub+1) // 2
            t += arr[i] * odd
        return t