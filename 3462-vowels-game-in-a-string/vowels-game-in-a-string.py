class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        for i in s:
            if i in vowels:
                return True
        return False