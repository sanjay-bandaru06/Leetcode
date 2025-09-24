class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted([int(d) for d in str(num)])
        num1 = ""
        num2 = ""
      
        for i, d in enumerate(digits):
            if i % 2 == 0:
                num1 += str(d)
            else:
                num2 += str(d)
        
        return int(num1) + int(num2)
