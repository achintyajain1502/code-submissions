# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l=""
        while head:
            l+=(str(head.val))
            head=head.next
        l=str(int(l)*2)
        dmy=ListNode(0)
        ptr=dmy
        for i in l:
            ptr.next=ListNode(int(i))
            ptr=ptr.next
        return dmy.next
        
        