class Solution:
    def reverseByType(self, s: str) -> str:
        letters = []
        special = []

        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                special.append(ch)

        letters = letters[::-1]
        special = special[::-1]

        result = ""
        i = 0  
        j = 0  

        for ch in s:
            if ch.isalpha():
                result += letters[i]
                i += 1
            else:
                result += special[j]
                j += 1

        return result