class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        max_str = s
        for ch in s:
            if ch != '9':
                max_str = s.replace(ch, '9')
                break

        min_str = s
        for ch in s:
            if ch != '0':
                min_str = s.replace(ch, '0')
                break

        return int(max_str) - int(min_str)