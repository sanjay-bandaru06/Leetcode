class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # if len(word1) != len(word2):
        #     return False
        r1 = "".join(word1)
        r2 = "".join(word2)

        if r1 == r2:
            return True
        else:
            return False
        
