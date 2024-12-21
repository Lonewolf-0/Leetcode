class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        i = 0
        while i+1<len(intervals):
            if intervals[i][1]>=intervals[i+1][0]:
                temp = max(intervals[i][1], intervals[i+1][1])
                intervals[i+1][1] = temp
                temp = min(intervals[i][0], intervals[i+1][0])
                intervals[i+1][0] = temp
                intervals.pop(i)
            else:
                i+=1
            
        return intervals







        print(intervals)