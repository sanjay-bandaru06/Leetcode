class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost[0],cost[1])

        prev2 , prev1  = cost[0], cost[1]
        
        for i in range(2,n):
            cur = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, cur
        return min(prev2,prev1)
