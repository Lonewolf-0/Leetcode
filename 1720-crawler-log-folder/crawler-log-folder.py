class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for i in logs:
            if i == '../':
                count-=1
                if count<0:
                    count=0
            elif i == './':
                count+=0
            else:
                count+=1
        return count
