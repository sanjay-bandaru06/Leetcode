class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        w = s.split()
        return " ".join(w[:k])
