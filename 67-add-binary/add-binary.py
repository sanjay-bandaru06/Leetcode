class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        carry=0
        tot=0
        res=[]
        while i>=0 or j>=0 or carry:
            tot=carry
            if i>=0:
                tot+=int(a[i])
                i-=1
            if j>=0:
                tot+=int(b[j])
                j-=1
            res.append(str(tot%2))
            carry = tot//2
        return ''.join(reversed(res))