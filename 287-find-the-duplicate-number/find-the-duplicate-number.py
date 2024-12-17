class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = set()
        for i in nums:
            if i in map:
                return i
            else:
                map.add(i)