class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def coun(n):
            s=0
            for i in range(1,n+1):
                s+=i
            return s

        if goal==0:
            c=0
            f=0
            flag=False
            if 0 not in nums:
                return 0
            for i in nums:
                if i==0:
                    c+=1
                else:
                    flag=True
                    f+=coun(c)
                    c=0
            if flag==False:
                return coun(len(nums))
            if c!=0:
                return f+coun(c)
                
        
        
        q=[-1]
        for i in range(len(nums)):
            if nums[i]:
                q.append(i)
        q.append(len(nums))

        i=0
        j=goal
        s=0
        while(j<len(q)-1):
            s+=(q[i+1]-q[i]-1)+(q[j+1]-q[j]-1)+1+((q[i+1]-q[i]-1)*(q[j+1]-q[j]-1))
            i+=1
            j+=1
            #print(s)
        return s
            

