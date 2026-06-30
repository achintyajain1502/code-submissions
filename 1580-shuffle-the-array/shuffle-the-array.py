class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        k=nums[:n]
        l=nums[n:]
        m=[]
        c=0
        while c<n:
            m.append(k[c])
            m.append(l[c])
            c+=1
        return m

        
        