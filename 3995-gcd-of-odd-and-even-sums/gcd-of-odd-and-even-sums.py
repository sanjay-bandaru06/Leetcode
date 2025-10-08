class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum = sum([2*i + 1 for i in range(n)])
        even_sum = sum([2*(i + 1) for i in range(n)])
        res = math.gcd(odd_sum, even_sum)
        return res