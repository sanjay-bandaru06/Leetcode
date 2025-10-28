class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        week_start = 1 

        while n > 0:
            for day in range(7):
                if n == 0:
                    break
                total += week_start + day
                n -= 1
            week_start += 1 
        return total