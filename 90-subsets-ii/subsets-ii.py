class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def subsets(i, sub):
            if i==n:
                sub.sort()
                if sub not in ans:
                    ans.append(sub)
                return

            subsets(i+1, sub)
            cub = sub.copy()
            cub.append(nums[i])
            subsets(i+1, cub)
        
        subsets(0, [])
        
        return ans
         
