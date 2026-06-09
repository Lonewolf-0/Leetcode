class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [(-1)]*(n)
        stack = []

        for i in range(0,2*n):
            j = i%n
            while(len(stack) and nums[stack[-1]]<nums[j]):
                ans[stack.pop()] = nums[j]
            if i<n :
                stack.append(j)

        return ans
        