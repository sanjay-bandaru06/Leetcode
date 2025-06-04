class Solution:
    def resultingString(self, s: str) -> str:
        st = []
        for i in s:
            if len(st) == 0:
                st.append(i)
            else:
                d = abs(ord(i) - ord(st[-1]))
                if d == 1 or d == 25:
                    st.pop()
                else:
                    st.append(i)
        return ''.join(st)