class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        result = []

        for i in range(len(code)):
            if isActive[i] and code[i] and businessLine[i] in order:
                ok = True
                for c in code[i]:
                    if not (c.isalnum() or c == "_"):
                        ok = False
                        break
                if ok:
                    result.append((order.index(businessLine[i]), code[i]))

        result.sort()
        return [c for _, c in result]