class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subseq(word, s):
            it = iter(s)
            return all(c in it for c in word)
        
        count = 0
        from collections import defaultdict
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        
        for word, cnt in word_count.items():
            if is_subseq(word, s):
                count += cnt
        return count