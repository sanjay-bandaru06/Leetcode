class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # l =[]
        # if n%2 & n%n == 0:
        #     l.append(n)
        # return sum(l)
        return n if n % 2 == 0 else n * 2