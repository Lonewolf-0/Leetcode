class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        n = len(goal)

        while n>0:
            n -= 1
            if s==goal:
                return True
            else:
                s = s[1:]+s[0]
        
        return False