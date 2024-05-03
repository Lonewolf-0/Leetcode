class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i=0
        j=0
        version1 = list(map(int, version1.split('.')))
        version2 = list(map(int, version2.split('.')))
        
        print(version1)
        print(version2)
        
        
        while i<len(version1) and j<len(version2):
            if version1[i]>version2[j]:
                return 1
            if version1[i]<version2[j]:
                return -1
            i+=1
            j+=1

        
        while i<len(version1):
            if version1[i]==0:
                i+=1
            else:
                return 1

        while j<len(version2):
            if version2[j]==0:
                j+=1
            else:
                return -1
        


        

        

        return 0
            