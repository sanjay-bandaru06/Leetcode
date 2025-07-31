class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        final = []
        for i in image:
            fliped = i[::-1]
            inverted = [1 - bit for bit in fliped]
            final.append(inverted)
        return final