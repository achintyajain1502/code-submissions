# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        l[k-1],l[-k]=l[-k],l[k-1]
        dmy=ListNode(0)
        ptr=dmy
        for i in l:
            ptr.next=ListNode(i)
            ptr=ptr.next
        return dmy.next