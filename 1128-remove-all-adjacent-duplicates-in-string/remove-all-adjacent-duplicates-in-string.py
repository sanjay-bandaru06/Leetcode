class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for i in s:
            if len(st) == 0:
                st.append(i)
            else:
                if i == st[-1]:
                    st.pop()
                else:
                    st.append(i)
        return ''.join(st)
