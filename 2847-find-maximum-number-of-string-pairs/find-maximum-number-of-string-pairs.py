class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        visited = set()

        for w in words:
            rev = w[::-1]      # reverse of the word

            if rev in visited:
                count += 1
            else:
                visited.add(w)

        return count