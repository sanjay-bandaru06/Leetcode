class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count  = 0
        for i in range(low , high + 1):
            s = str(i)
            if len(s) % 2 == 1:
                continue
            n = len(s) // 2
            left_sum = sum(int(ch) for ch in s[:n])
            right_sum = sum(int(ch) for ch in s[n:])
            if left_sum == right_sum:
                count += 1
        return count
