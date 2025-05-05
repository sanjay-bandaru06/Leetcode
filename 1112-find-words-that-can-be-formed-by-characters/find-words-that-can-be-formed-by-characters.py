class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        k = Counter(chars)
        for i in words:
            if Counter(i) <= k:
                count += len(i)
        return count