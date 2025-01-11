class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = c2 = 0
        el1, el2 = float('-inf'), float('-inf') # element 1 and element 2

        for i in range(len(nums)):
            if c1 == 0 and el2 != nums[i]:
                c1 = 1
                el1 = nums[i]
            elif c2 == 0 and el1 != nums[i]:
                c2 = 1
                el2 = nums[i]
            elif nums[i] == el1:
                c1+=1
            elif nums[i] == el2:
                c2+=1 
            else:
                c1-=1
                c2-=1
        ls = [] 
        cnt1, cnt2 = 0, 0
        for i in range(len(nums)):
            if nums[i] == el1:
                cnt1 += 1
            if nums[i] == el2:
                cnt2 += 1

        mini = int(len(nums) / 3) + 1
        if cnt1 >= mini:
            ls.append(el1)
        if cnt2 >= mini:
            ls.append(el2)

        # Uncomment the following line
        # if it is told to sort the answer array:
        #ls.sort() #TC --> O(2*log2) ~ O(1);

        return ls