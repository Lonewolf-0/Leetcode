class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        destroyed = False
        for i in asteroids:
            if i>0 :
                stack.append(i)
            else:
                while len(stack)!=0 and stack[-1]>0 and stack[-1] <= abs(i):
                    if stack[-1] == abs(i):
                        stack.pop()
                        destroyed = True
                        break
                    stack.pop()
                if (len(stack)==0 or stack[-1]<0) and not destroyed:
                    stack.append(i)
                destroyed = False
        return stack