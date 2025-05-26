class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for i in row:
                if i < 0:
                    count += 1
        return count