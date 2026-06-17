class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []
        
        for i in range(n - k + 1):
            window = nums[i:i+k]
            
            freq = Counter(window)
            
            sorted_items = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))
            
            top_x = sorted_items[:x]
            
            x_sum = sum(val * count for val, count in top_x)
            result.append(x_sum)
        
        return result