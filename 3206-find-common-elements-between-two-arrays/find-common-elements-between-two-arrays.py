class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        a1 = 0
        for x in nums1:
            if x in set2:
                a1 += 1

        a2 = 0
        for x in nums2:
            if x in set1:
                a2 += 1

        return [a1, a2]