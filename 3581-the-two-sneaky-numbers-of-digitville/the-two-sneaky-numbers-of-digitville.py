class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # count = {}
        # l = []
        # for i in range(0, len(nums)-1):
        #     if i in count:
        #         count[i] += 1
        #     else:
        #         count[i] = 1
        # print(count)
        # for i in count:
        #     if count[i] == 2:
        #         l.append(count)
        # return l

        


        count = defaultdict(int)
        l = []
        for i in range(0, len(nums)):
                if nums[i] in count:
                    count[nums[i]] += 1
                else:
                    count[nums[i]] = 1

        for j in count:
            if count[j] >= 2:
                l.append(j)
        return l