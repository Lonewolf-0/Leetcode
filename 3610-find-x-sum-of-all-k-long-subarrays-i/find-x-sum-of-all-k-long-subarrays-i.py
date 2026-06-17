class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        freq = defaultdict(int)
        heap = []
        result = []
        
        # Initialize first window
        for i in range(k):
            freq[nums[i]] += 1
        for val, count in freq.items():
            heapq.heappush(heap, (-count, -val, val))
        
        def get_xsum():
            seen = set()
            total = 0
            temp = []
            while len(seen) < x and heap:
                f, vneg, val = heapq.heappop(heap)
                count = -f
                # Validate against current frequency
                if freq.get(val, 0) == count and val not in seen:
                    total += val * count
                    seen.add(val)
                temp.append((f, vneg, val))
            # Push back all popped items
            for item in temp:
                heapq.heappush(heap, item)
            return total
        
        result.append(get_xsum())
        
        # Slide the window
        for i in range(k, n):
            out_elem = nums[i-k]
            in_elem = nums[i]
            
            # Update outgoing
            freq[out_elem] -= 1
            if freq[out_elem] == 0:
                del freq[out_elem]
            heapq.heappush(heap, (-freq.get(out_elem, 0), -out_elem, out_elem))
            
            # Update incoming
            freq[in_elem] += 1
            heapq.heappush(heap, (-freq[in_elem], -in_elem, in_elem))
            
            result.append(get_xsum())
        
        return result