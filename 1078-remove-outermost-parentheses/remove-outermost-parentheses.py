class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        d = 0
        for ch in s:
            if ch == '(':
                if d > 0:
                    res.append(ch)
                d += 1
            elif ch == ')':
                d -= 1
                if d > 0:
                    res.append(ch)
        return "".join(res)