class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = 0
        subarraySums = {0 : 1}
        prefixSum = 0
        
        for num in nums:
            prefixSum += num

            if prefixSum-k in subarraySums:
                subarrays += subarraySums[prefixSum - k]
            
            if prefixSum not in subarraySums:
                subarraySums[prefixSum] = 1
            else:
                subarraySums[prefixSum] += 1

        return subarrays