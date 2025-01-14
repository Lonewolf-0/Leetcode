class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        ans = ""
        for i in range(n):
            for j in range(i,n):
                temp = s[i:j+1]
                # print(temp)
                if temp == temp[::-1]:
                    if len(temp)>len(ans):
                        ans = temp
        return ans
        