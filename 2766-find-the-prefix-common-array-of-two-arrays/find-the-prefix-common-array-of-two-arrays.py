class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        s = set()
        ans = []
        for i in range(n):
            s.add(A[i])
            s.add(B[i])
            ans.append(2*(i+1) - len(s))


        return ans

