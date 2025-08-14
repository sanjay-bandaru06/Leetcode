class Solution:
    def largestGoodInteger(self, num: str) -> str:
        mx = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                if mx == "" or num[i:i+3] > mx:
                    mx = num[i:i+3]
        return mx