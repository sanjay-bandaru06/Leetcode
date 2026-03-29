class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        v = set('aeiou')
        i = len(s) - 1
        while i >= 0 and s[i] in v:
            i -= 1
        return s[:i+1]