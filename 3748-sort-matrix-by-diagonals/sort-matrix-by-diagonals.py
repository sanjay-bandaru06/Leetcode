class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        for row in range(n):
            i, j = row, 0
            diag = []

            while i < n and j < n:
                diag.append(grid[i][j])
                i += 1
                j += 1

            diag.sort(reverse=True)

            i, j = row, 0
            idx = 0
            while i < n and j < n:
                grid[i][j] = diag[idx]
                idx += 1
                i += 1
                j += 1

        for col in range(1, n):
            i, j = 0, col
            diag = []

            while i < n and j < n:
                diag.append(grid[i][j])
                i += 1
                j += 1

            diag.sort()

            i, j = 0, col
            idx = 0
            while i < n and j < n:
                grid[i][j] = diag[idx]
                idx += 1
                i += 1
                j += 1

        return grid