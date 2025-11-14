class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        curr = 0
        
        for g in gain:
            curr += g
            max_alt = max(max_alt, curr)
        
        return max_alt