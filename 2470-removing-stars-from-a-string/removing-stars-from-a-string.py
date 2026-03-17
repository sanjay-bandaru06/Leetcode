class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for ch in s:
            if ch =='*':
                st.pop()
            else:
                st.append(ch)
        return "".join(st)