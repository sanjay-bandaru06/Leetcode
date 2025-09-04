class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        half = n // 2
        
        freq = Counter(arr)
        counts = sorted(freq.values(), reverse=True)
        
        removed, size = 0, 0
        for c in counts:
            removed += c
            size += 1
            if removed >= half:
                return size