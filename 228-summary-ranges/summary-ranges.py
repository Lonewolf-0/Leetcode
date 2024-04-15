class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        
        if len(nums)==0:
            return nums
        if len(nums)==1:
            return [str(nums[0])]
        low = nums[0]
        high = nums[0]
        ans = []
        nums.append(0)
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                high+=1
            else:
                if low != high:
                    ans.append(str(low)+'->'+str(high))
                else:
                    ans.append(str(low))
                low = nums[i+1]
                high = nums[i+1]
        
        return ans

