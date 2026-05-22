class Solution(object):

    def qs(self, nums, l, r):

        def partition(nums, l, r):

            pivot = nums[r]

            i = l - 1

            for j in range(l, r):

                if nums[j] <= pivot:

                    i += 1

                    nums[i], nums[j] = nums[j], nums[i]

            nums[i+1], nums[r] = nums[r], nums[i+1]

            return i + 1


        if l < r:

            q = partition(nums, l, r)

            self.qs(nums, l, q-1)

            self.qs(nums, q+1, r)


    def sortColors(self, nums):

        self.qs(nums, 0, len(nums)-1)

        return nums

        # return(nums.sort())