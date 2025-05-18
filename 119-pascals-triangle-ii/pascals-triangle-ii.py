class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            row = [a + b for a, b in zip([0] + row, row + [0])]
        return row