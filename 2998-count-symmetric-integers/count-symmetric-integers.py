class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric_number(num):
            s = str(num)
            if len(s) % 2 != 0:
                return False
            half = len(s) // 2
            first_half = s[:half]
            second_half = s[half:]
            return sum(map(int, first_half)) == sum(map(int, second_half))

        def find_symmetric(x):
            result = []
            for i in range(10, x + 1):  # Skip single digits
                if is_symmetric_number(i):
                    result.append(i)
            return len(result)
        
        return find_symmetric(high)-find_symmetric(low-1)