class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        result = left = 0

        for right in range(0, len(s), 1):
            right_char = s[right]

            if (right_char in char_map):
                left = max(left, char_map[right_char] + 1)
            

            char_map[right_char] = right
            result = max(result, right - left + 1)

        return result
        