class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(s.startswith(pref) for s in words)
        