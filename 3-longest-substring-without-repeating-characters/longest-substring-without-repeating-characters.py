class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        ans = 0
        
        for j in range(len(s)):
            for i in range(j, len(s)):    
                if s[i] in a:
                    ans = max(ans, len(a))
                    a.clear()
                    break
                else:
                    a.add(s[i])
                   
            
        ans = max(ans, len(a))
                    
        return ans

        