class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        unequal = 0
        arr1 = []
        arr2 = []
        if s1==s2:
            return True

        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                unequal+=1
                arr1.append(s1[i])
                arr2.append(s2[i])
            
            if unequal>2:
                return False
        if unequal == 2:
            arr1.sort()
            arr2.sort()
            if arr1==arr2:
                return True
            else:
                return False
        return False
        