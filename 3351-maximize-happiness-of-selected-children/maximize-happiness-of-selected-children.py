class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        ans = 0
        
        for i in range(k-1):
            if happiness[i]>0:
                ans+=happiness[i]
            happiness[i+1]-=i+1
            
        if happiness[k-1]>0:
            ans+=happiness[k-1]
            
            

        # for i in range(k):
        #     if happiness[i+1]>0:
        #         ans+=happiness[i]
            
            
        #     happiness[i+1]-=i+1
        
        return ans

