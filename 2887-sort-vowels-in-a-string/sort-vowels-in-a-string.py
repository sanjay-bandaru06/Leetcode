class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        res = []
        idx = 0
        sorted_itm  = sorted(ch for ch in s if ch in vowels)

        for ch in s:
            if ch in vowels:
                res.append(sorted_itm[idx])
                idx += 1
            else:
                res.append(ch)
        

        return "".join(res)