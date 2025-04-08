class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        # if x % 2 == 0:
        #     return x//2
        # else:
        #     return -1
        sum = 0
        temp = x
        while temp > 0:
            sum += temp % 10
            temp //= 10
        if x % sum == 0:
            return sum
        else:
            return -1
        