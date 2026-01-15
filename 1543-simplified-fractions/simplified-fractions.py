class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        
        for d in range(2, n + 1):
            for n in range(1, d):
                if math.gcd(n, d) == 1:
                    res.append(f"{n}/{d}")
        
        return res