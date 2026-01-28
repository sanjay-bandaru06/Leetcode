class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = ["0", "1"]
        
        for i in range(n - 1):
            new = []
            for s in res:
                new.append(s + "1")
                if s[-1] != "0":
                    new.append(s + "0")
            res = new
        
        return res