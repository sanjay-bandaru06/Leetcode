class Solution:
    def minSteps(self, s: str, t: str) -> int:
        steps = 0
        for c in set(s):
           steps += max(0, s.count(c) - t.count(c))

        return steps