class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        equal = []
        r = []
        
        for num in nums:
            if num < pivot:
                l.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                r.append(num)
        
        return l + equal + r