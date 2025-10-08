class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # a = int("".join(map(str,num)))
        # dig = a+k
        # dig = [int(d) for d in str(dig)]
        # return dig

        res = []
        i = len(num) - 1
        carry = k

        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]
                i -= 1
            res.append(carry % 10)
            carry //= 10

        return res[::-1]