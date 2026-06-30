# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        l=[]
        while head!=None:
            if head.val==val:
                head=head.next
            else:
                l.append(head.val)
                head=head.next
        dummy=ListNode(0)
        ptr=dummy
        for i in l:
            ptr.next=ListNode(i)
            ptr=ptr.next
        return dummy.next
        