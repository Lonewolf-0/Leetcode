class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        

        curr = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                curr+=nums[i]
                ans = max(ans, curr)
            else:
                curr=nums[i]
        return ans

