class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sets = set(nums)
        l = []
        for i in range(1,n+1):
            if i not in sets:
                l.append(i)
        return l

            
