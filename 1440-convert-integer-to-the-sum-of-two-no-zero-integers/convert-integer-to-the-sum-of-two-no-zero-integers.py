class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # if n > 1:
        #     a = 1
        #     b = n - 1
        # elif n < -1:
        #     a = -1
        #     b = n + 1
        # elif n == 1:
        #     a, b = 2, -1
        # elif n == -1:
        #     a, b = -2, 1  
        # else:  
        #     a, b = 1, -1  
        # return a, b


        for a in range(1, n):
            b = n - a
            if "0" not in str(a) and "0" not in str(b):
                return [a, b]

        