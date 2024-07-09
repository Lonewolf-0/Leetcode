class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        prev = 0
        curr = customers[0][0]
        total = 0
        for i in range(n):

            

            if curr >= customers[i][0]:
                curr += customers[i][1]
                
            else:
                curr = customers[i][0] + customers[i][1]
            total += (curr -customers[i][0])
            
            print(curr)
            print(total)
        
        return total/n


