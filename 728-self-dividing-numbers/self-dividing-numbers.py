class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            s = str(i)
            valid = True
            for ch in s:
                d = int(ch)
                if d == 0 or i % d != 0:
                    valid = False    
                    break
            if valid:
                res.append(i)
        return res