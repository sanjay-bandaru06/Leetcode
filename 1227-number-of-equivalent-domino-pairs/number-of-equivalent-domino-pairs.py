class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # 10^4 = 10000
        count = 0
        # for i in range(len(dominoes)):
        #     for j in range(i + 1, len(dominoes)):
        #         if (dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]) or \
        #            (dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]):
        #             count += 1

        freq = [0] * 100
        for a, b in dominoes:
            key = a * 10 + b if a <= b else b * 10 + a
            count += freq[key]
            freq[key] += 1
        return count