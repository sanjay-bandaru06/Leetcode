class Solution:
    def smallestNumber(self, n: int) -> int:
        b = bin(n)[2:]
        return int('1' * len(b), 2)