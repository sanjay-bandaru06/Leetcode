class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        b = set(brokenLetters)
        for w in text.split():
            if not any(ch in b for ch in w):
                count += 1
        return count