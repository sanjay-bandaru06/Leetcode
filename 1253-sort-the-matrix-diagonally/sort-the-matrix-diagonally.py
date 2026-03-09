class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        diag = defaultdict(list)

        for r in range(m):
            for c in range(n):
                diag[r - c].append(mat[r][c])

        for d in diag:
            diag[d].sort(reverse=True)

        for r in range(m):
            for c in range(n):
                mat[r][c] = diag[r - c].pop()

        return mat