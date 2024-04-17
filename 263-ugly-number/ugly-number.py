class Solution:
    def isUgly(self, n: int) -> bool:
         
        res = []
        if n<=0:
            return False
        while n % 2 == 0:
            res.append(2)
            n = n // 2
            
        for i in range(3,int(math.sqrt(n))+1,2):
            
            while n % i== 0:
                if i not in [2,3,5]:
                    return False
                res.append(i)
                n = n // i
                    
            
        if n > 2:
            if n not in [2,3,5]:
                return False
            res.append(n)
        return True
        

                