class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        tot = 0
        
        for ch in s:
            tot += abs(s.index(ch) - t.index(ch))
        
        return tot