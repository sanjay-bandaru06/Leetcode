class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        j = set(jewels)
        for s in stones:
            if s in j:
                count += 1
        return count
