class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        
        # return right - left
        v = set('aeiou')
        count = 0
        
        for i in range(left, right + 1):
            word = words[i]
            
            if word[0] in v and word[-1] in v:
                count += 1
                
        return count