class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n)[2:]
        
        res = ''
        for i in b:
            if  i == '1':
                res += '0'
            else:
                res += '1'

        return int(res, 2)