class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for curr_size in range(n, 1, -1):
            max_idx = arr.index(max(arr[:curr_size]))
            if max_idx != curr_size - 1:
                if max_idx != 0:
                    res.append(max_idx + 1)
                    arr[:max_idx + 1] = reversed(arr[:max_idx + 1])
                res.append(curr_size)
                arr[:curr_size] = reversed(arr[:curr_size])
        return res






