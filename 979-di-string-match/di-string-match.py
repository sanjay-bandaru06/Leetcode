class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l = 0
        h = len(s)
        perm = []

        for ch in s:
            if ch == 'I':
                perm.append(l)
                l += 1
            else:  
                perm.append(h)
                h -= 1

        perm.append(l)  
        return perm