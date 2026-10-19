class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        l=[]
        c=0
        e=0
        for i in nums:
            if i==target:
                e+=1
            elif i<target:
                c+=1
        for i in range(c,c+e):
            l.append(i)
        return l
        # nums.sort()
        # l=[]
        # for i in range(len(nums)):           O(nlogn)
        #     if nums[i]==target:
        #         l.append(i)
        # return l
