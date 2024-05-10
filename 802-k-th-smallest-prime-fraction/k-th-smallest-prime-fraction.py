class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        minHeap = []
        N = len(arr)
        
        for i in range(N):
            for j in range(i + 1, N):
                fraction = (arr[i] / arr[j], (arr[i], arr[j]))
                heappush(minHeap, fraction)
        
        for _ in range(k - 1):
            heappop(minHeap)
        
        return heappop(minHeap)[1]
        