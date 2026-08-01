class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l={}
        m={}
        k=[]
        for i in nums1:
            if i not in l:
                l[i]=1
            else:
                l[i]+=1
        for i in nums2:
            if i not in m:
                m[i]=1
            else:
                m[i]+=1
        for i in l:
            if i in m:
                for o in range(min(l[i],m[i])):
                    k.append(i)
        return k
        