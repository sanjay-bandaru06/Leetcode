class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        num = []
        for i in range(1, n + 1):
            num.append(i)
        num.sort(key=str)
        return num