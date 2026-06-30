# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        l=[]
        m=ListNode(0)
        ptr=m
        while head!=None:
            l.append(head.val)
            head=head.next
        n=len(l)
        k%=n
        l.reverse()
        l[:k]=reversed(l[:k])
        l[k:]=reversed(l[k:])
        for i in l:
            ptr.next=ListNode(i)
            ptr=ptr.next
        return m.next
        