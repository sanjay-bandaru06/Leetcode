class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        stack = [(0, [], 0)]
        while stack:
            i, cur, total = stack.pop()
            if total == target:
                res.append(cur)
                continue
            if i >= len(candidates) or total > target:
                continue
            stack.append((i, cur + [candidates[i]], total + candidates[i]))
            stack.append((i + 1, cur, total))
        return res