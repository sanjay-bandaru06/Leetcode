class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        
        rank = {}
        for i in range(len(sorted_arr)):
            rank[sorted_arr[i]] = i + 1 
        
        l = []
        for num in arr:
            l.append(rank[num])
        
        return l