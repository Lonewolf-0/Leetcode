class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev = 0
        curr = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i]==0:
                ans = max(ans,prev+curr)
                prev = curr
                curr = 0
            else:
                curr+=1

        if curr == len(nums):
            return len(nums)-1
        ans = max(ans,prev+curr)
        return ans