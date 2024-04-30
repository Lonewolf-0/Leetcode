class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0 for _ in range(1024)]
        result = 0
        prefix = 0
        count[prefix] = 1

        for i in word:
            char_index = ord(i)-ord('a')
            prefix ^= 1<<char_index
            result+=count[prefix]
            for i in range(10):
                result+=count[prefix ^ (1<<i)]
            count[prefix]+=1

        return result

