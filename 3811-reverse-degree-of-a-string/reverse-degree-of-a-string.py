class Solution:
    def reverseDegree(self, s: str) -> int:
        tot = 0
        for i, ch in enumerate(s):
            tot += (ord('z') - ord(ch) + 1) * (i + 1)
        return tot