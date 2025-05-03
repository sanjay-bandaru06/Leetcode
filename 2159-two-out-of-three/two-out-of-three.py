class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        l =[]
        k = set(nums1 + nums2 + nums3)
        for i in k:
            count = 0
            if i in nums1:
                count += 1
            if i in nums2:
                count += 1
            if i in nums3:
                count += 1
            if count >= 2:
                l.append(i)
        return l