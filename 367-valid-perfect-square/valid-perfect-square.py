class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        root = int(math.sqrt(num))
        return root * root == num