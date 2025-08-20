class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ar =[]
        for i in range(len(nums)):
            ar.insert(index[i], nums[i]) 
        return ar
