class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        f = set(friends)
        res = []

        for p in order:
            if p in f:
                res.append(p)

        return res