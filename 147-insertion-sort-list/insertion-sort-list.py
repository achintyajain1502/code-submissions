# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l=[]
        while head!=None:
            l.append(head.val)
            head=head.next
        l.sort()
        dummy=ListNode(0)
        ptr=dummy
        for i in l:
            ptr.next=ListNode(i)
            ptr=ptr.next
        return dummy.next