class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        count = 0
        for i in s:
            if i == letter:
                count +=1
        # return (int(count)/int(n))*100
        return (count * 100) // n
