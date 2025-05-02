class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = [("", 0, 0)]

        while stack:
            s, open_c, close_c = stack.pop()
            if open_c == n and close_c == n:
                res.append(s)
            if open_c < n:
                stack.append((s + "(", open_c + 1, close_c))
            if close_c < open_c:
                stack.append((s + ")", open_c, close_c + 1))

        return res