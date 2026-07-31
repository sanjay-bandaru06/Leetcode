class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        return sum(int(i) for i in str(n))