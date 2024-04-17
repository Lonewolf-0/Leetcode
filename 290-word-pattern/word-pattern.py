class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        
        if len(s)!=len(pattern):
            return False
        
        d = {}
        se = set()

        for i in range(len(pattern)):
            if pattern[i] in d :
                if d[pattern[i]]!=s[i]:
                    return False
            else:
                if s[i] not in se:
                    d[pattern[i]]=s[i]
                    se.add(s[i])
                else:
                    return False
        
        return True
        
                