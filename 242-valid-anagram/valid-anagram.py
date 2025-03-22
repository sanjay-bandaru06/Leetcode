class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for i in range(len(s)):
        #     for j in range(len(t)):
        #         if s[i] == t[j]:

        #             return True
        #             continue
        # return False

        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)