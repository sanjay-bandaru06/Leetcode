class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        suffixSum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffixSum[i] = suffixSum[i + 1] + piles[i]
        
        @lru_cache(None)
        def dfs(i, M):
       
            if i + 2 * M >= n:
                return suffixSum[i]
            
            max_stones = 0
            
            for X in range(1, 2 * M + 1):
                opponent = dfs(i + X, max(M, X))
                current = suffixSum[i] - opponent
                max_stones = max(max_stones, current)
            
            return max_stones
        
        return dfs(0, 1)