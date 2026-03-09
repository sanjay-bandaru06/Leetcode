class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for r in grid:
            r.sort()

        ans = 0

        for c in range(len(grid[0])):
            mx = 0
            for r in range(len(grid)):
                mx = max(mx, grid[r][c])
            ans += mx

        return ans