class Solution:
    def concatHex36(self, n: int) -> str:
        h = hex(n * n)[2:].upper()
        cube = n * n * n
        chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base36_value = ""
        
        while cube > 0:
            base36_value = chars[cube % 36] + base36_value
            cube //= 36

        return h + base36_value