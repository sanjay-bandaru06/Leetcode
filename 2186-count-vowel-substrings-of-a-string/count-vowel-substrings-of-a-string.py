class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        res = 0
        v = set('aeiou')
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if word[j] not in v:
                    break
                seen.add(word[j])
                if len(seen) == 5:
                    res += 1
        return res

