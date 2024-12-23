class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = 0
        subarraySums = {0 : 1}
        prefixSum = 0
        for num in nums:
            prefixSum += num
            subarrays += subarraySums.get(prefixSum - k, 0)
            subarraySums[prefixSum] = subarraySums.get(prefixSum, 0) + 1
        return subarrays