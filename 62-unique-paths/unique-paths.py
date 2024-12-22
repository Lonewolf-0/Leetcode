class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = 1

        for i in range(m-1):
            ans = (ans * (n + i)) // (i+1)



        return ans