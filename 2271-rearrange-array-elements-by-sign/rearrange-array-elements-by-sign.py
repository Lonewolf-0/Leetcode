class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        ans = []

        for i in nums:
            if i>=0:
                arr1.append(i)
            else:
                arr2.append(i)

        print(arr1,arr2)

        for i in range(len(nums)//2):
            ans.append(arr1[i])
            ans.append(arr2[i])

        return ans



        