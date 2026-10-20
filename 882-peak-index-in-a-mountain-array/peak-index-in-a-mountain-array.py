class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l=0
        r=len(arr)-1
        while l<r:
            q=(l+r)//2
            if arr[q]>arr[q+1] and arr[q]>arr[q-1]:
                return q
            elif arr[q]>arr[q+1] and arr[q]<arr[q-1]:
                r=q
            else:
                l=q
        