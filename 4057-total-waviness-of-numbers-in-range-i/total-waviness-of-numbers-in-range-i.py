class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def getWaviness(num: int) -> int:
            s = str(num)
            if len(s) < 3:
                return 0
            
            waviness = 0

            for i in range(1, len(s) - 1):
                curr = int(s[i])
                left = int(s[i - 1])
                right = int(s[i + 1])

                if curr > left and curr > right:
                    waviness += 1
          
                elif curr < left and curr < right:
                    waviness += 1
            
            return waviness

        total = 0
        for num in range(num1, num2 + 1):
            total += getWaviness(num)
        
        return total
            