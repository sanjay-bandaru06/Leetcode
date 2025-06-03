class Solution:
    def isValid(self, s: str) -> bool:
        
        # stack = []
        # p = {')':'(',']':'[','}':'{'}
        # for char in s:
        #     if char in p:
        #         if not stack or stack.pop() != p[char]:
        #             return False
        #     else:
        #         stack.append(char)
        # return not stack

        for i in range(len(s)):
            s = s.replace('{}', '').replace('[]', '').replace('()', '')
        return s == ''



        