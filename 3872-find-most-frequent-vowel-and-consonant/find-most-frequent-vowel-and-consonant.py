class Solution:
    def maxFreqSum(self, s: str) -> int:
        c1,c2 = 0,0
        vowels = "aeiouAEIOU"
        cons = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNOPQRSTVWXYZ'
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        for v in vowels:
            if v in freq:
                c1 = max(c1, freq[v])

        for c in cons:
            if c in freq:
                c2 = max(c2, freq[c])

        return c1+c2

