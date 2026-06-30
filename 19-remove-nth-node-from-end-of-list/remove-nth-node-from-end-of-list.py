# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        ptr=dummy
        l=[]
        while head!=None:
            l.append(head.val)
            head=head.next
        del l[-n]
        for i in l:
            ptr.next=ListNode(i)
            ptr=ptr.next
        return dummy.next
        
        