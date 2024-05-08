class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        d = dict()
        arr = []

        for i in range(len(score)):
            count = 0
            for j in range(len(score)):
                if score[i]<=score[j]:
                    count+=1
            if count ==1:
                arr.append('Gold Medal')
            elif count == 2:
                arr.append('Silver Medal')
            elif count == 3:
                arr.append('Bronze Medal')
            else:
                arr.append(str(count))

        return arr
            
            
