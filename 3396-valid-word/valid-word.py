class Solution:
    def isValid(self, word: str) -> bool:
        vowels = set('aeiouAEIOU')
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False

        for ch in word:
            if not ch.isalnum():
                return False

            if ch.isalpha():
                if ch in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
        
        if has_vowel and has_consonant:
            return True
        else:
            return False