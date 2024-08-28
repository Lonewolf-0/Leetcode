class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        d1 = dict(Counter(s1))
        d2 = dict(Counter(s2[:l1]))
        if d1==d2 :
            return True

        for i in range(l1, l2):
            if d1==d2 :
                return True
            
            if s2[i] in d2.keys():
                d2[s2[i]]+=1
            else:
                d2[s2[i]]=1
            
            d2[s2[i-l1]]-=1
            if d2[s2[i-l1]] == 0:
                del d2[s2[i-l1]]

        if d1==d2:
            return True
        
        return False