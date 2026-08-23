# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        l=[]
        k=[]
        while head:
            l.append(head.val)
            head=head.next
        for j in range(len(l)-1):
            k.append(l[j])
            k.append(gcd(l[j],l[j+1]))
        k.append(l[-1])
        l=ListNode(0)
        ptr=l
        for i in k:
            ptr.next=ListNode(i)
            ptr=ptr.next
        return l.next