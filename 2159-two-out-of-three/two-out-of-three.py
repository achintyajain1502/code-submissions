class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        r=[]
        for i in nums1:
            if i in nums2:
                r.append(i)
            if i in nums3:
                r.append(i)
        for i in nums3:
            if i in nums2:
                r.append(i)
        return list(set(r))