class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i in range(26):
            d[order[i]] = i

        def get_key(word):
            return [ d[c] for c in word ]
        
        return words == sorted(words, key=get_key)
            