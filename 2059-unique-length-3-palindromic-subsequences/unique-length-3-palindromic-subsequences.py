class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = [0]*26
        right = [0]*26

        for i in s:
            right[ord(i)-97]+=1
        S = set()

        for i in range(len(s)):
            t = ord(s[i]) - 97
            right[t] -= 1
            for j in range(26):
                if left[j] > 0 and right[j] > 0:
                    S.add(26*t+j)
            left[t]+=1
        
        return len(S)