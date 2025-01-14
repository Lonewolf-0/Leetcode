class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        def expand(left,right,n):

            while left>=0 and right <n and s[left] == s[right]:
                left -=1
                right +=1

            return right-left - 1, s[left+1:right]
        maxlen = 0
        sub = ""
        for i in range(n):

            len1, sub1 = expand(i,i,n)
            len2, sub2 = expand(i,i+1,n)

            if len1 > maxlen:
                sub = sub1
                maxlen = len1
            if len2 > maxlen:
                sub = sub2
                maxlen = len2

        return sub
            

                
        