class Solution:
    def minimumLength(self, s: str) -> int:
        d = dict(Counter(s))
        n = len(s)

        for i in d.values():
            if i>=3:
                if i%2==0:
                    n-= (i-2)
                else:
                    n-= (i-1)
        return n
