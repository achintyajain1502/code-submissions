class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums1[:]=nums1[:m]+nums2  #same list num1 modified
        nums1.sort()


        # nums1=nums1+nums2 [creates new list]
        # nums1+nums2       [does nothing nums1 remains as it is]
        # nums1.sort()
        # l=nums1.count(0)
        # for i in range(l):
        #     nums1.remove(0)
        # print(nums1)
             
