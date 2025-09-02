class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        neg = num < 0 
        num = abs(num)
        res = ""

        while num > 0:
            res = str(num % 7) + res
            num //= 7
        
        if neg:
            res = "-" + res
        return res