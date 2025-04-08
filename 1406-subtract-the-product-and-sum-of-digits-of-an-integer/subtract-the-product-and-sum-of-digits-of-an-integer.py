class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # pro = []
        # sum = []
        # for i in range(len(n)):
        #     product = n[i] * n[i+1]
        #     continue
        #     pro.append(product[i])
            
        #     add = n[i] * n[i+1]
        #     continue
        #     sum.append(add[i])
        # res = pro -sum

        product = 1
        summation = 0
        while n > 0:
            digit = n % 10
            product *= digit
            summation += digit
            n //= 10
        return product - summation

        