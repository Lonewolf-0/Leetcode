class Solution:
    def trap(self, height: List[int]) -> int:
        arr = []
        arr.append([height[0]])
        for i in range(1,len(height)):
            arr.append([max(arr[i-1][0], height[i])])
        arr[-1].append(height[-1])
        # print(arr)
        for i in range(len(height)-2, -1, -1):
            arr[i].append(max(arr[i+1][1], height[i]))
        
        count = 0
        # print(arr)
        for i in range(len(height)):
            count+=min(arr[i][0], arr[i][1]) - height[i]
        
        return count

        