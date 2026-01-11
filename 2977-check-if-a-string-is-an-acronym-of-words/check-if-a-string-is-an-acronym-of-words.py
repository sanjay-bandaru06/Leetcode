class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        a = ""
        for word in words:
            a += word[0]
        return a == s