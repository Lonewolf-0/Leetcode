class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        freq = defaultdict(int)
        result = []
        
        for i in range(k):
            freq[nums[i]] += 1
        
        def compute_xsum():
            top = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))[:x]
            return sum(val * count for val, count in top)
        
        result.append(compute_xsum())
        
        for i in range(k, n):
            out_elem = nums[i-k]
            in_elem = nums[i]
            
            freq[out_elem] -= 1
            if freq[out_elem] == 0:
                del freq[out_elem]
            freq[in_elem] += 1
            
            result.append(compute_xsum())
        
        return result