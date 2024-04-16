class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return True if(word.upper()==word or word.lower()==word or word[1:].lower()==word[1:]) else False