class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def combinations(sub, i, target):
            if i==len(candidates):
                if target==0:
                    ans.append(sub)
                return

            if candidates[i]<=target:
                cub = sub.copy()
                cub.append(candidates[i])
                combinations(cub, i,target-candidates[i])
                
            combinations(sub, i+1, target)

        combinations([], 0, target)
        return ans
