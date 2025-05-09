class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro = 1
        sum = 0
        while n > 0:
            r = n % 10
            pro *= r
            sum += r
            n //= 10
        return pro - sum

        