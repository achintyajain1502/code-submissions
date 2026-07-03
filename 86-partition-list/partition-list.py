# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        l=[]
        r=[]
        while head!=None:
            if head.val<x:
                l.append(head.val)
                head=head.next
            else:
                r.append(head.val)
                head=head.next
        l=l+r
        dummy=ListNode(0)
        ptr=dummy
        for i in l:
            ptr.next=ListNode(i)
            ptr=ptr.next
        return dummy.next
        