class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse = True)
        ans = 0

        while( len(people)>1):
            if people[0]+people[-1]<=limit:
                ans+=1
                people.pop(0)
                people.pop()
                
            else:
                people.pop(0)
                ans+=1
        if len(people):
            ans+=1
        
        return ans