class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        m = len(g)
        n = len(s)
        child = 0
        cookie = 0
        childcount = 0

        while(child<m and cookie<n):
            if s[cookie]>=g[child]:
                childcount+=1
                child+=1
            cookie+=1
        return childcount


        