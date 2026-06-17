class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []
        
        for i in range(n - k + 1):
            window = nums[i:i+k]
            
            freq = Counter(window)
            
            # Step 3: Sort by (frequency desc, value desc)
            sorted_items = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))
            
            # Step 4: Take top x elements
            top_x = sorted_items[:x]
            
            # Step 5: Compute X-Sum
            x_sum = sum(val * count for val, count in top_x)
            result.append(x_sum)
        
        return result