class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        k=nums1+nums2
        k.sort()
        print k
        if len(k)%2!=0:
            return k[len(k)/2]
        else:
            return (k[len(k)//2]+k[len(k)/2 -1])/2.0
