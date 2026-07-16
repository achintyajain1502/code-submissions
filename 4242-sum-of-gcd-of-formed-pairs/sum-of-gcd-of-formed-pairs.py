class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixGcd=[]
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        m=0
        for i in range(len(nums)):
            m=max(m,nums[i])
            prefixGcd.append(gcd(nums[i],m))
        prefixGcd.sort()
        n=len(prefixGcd)
        i=0
        j=len(nums)-1
        s=0
        while i<j:
            s+=gcd(prefixGcd[i],prefixGcd[j])
            i+=1
            j-=1
        return s
            
        