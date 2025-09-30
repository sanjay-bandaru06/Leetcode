class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}
        for num in range(1, n + 1):
            s = 0
            x = num
            while x > 0:
                s += x % 10
                x //= 10
            if s in groups:
                groups[s] += 1
            else:
                groups[s] = 1
        max_size = max(groups.values())
        return sum(1 for size in groups.values() if size == max_size)