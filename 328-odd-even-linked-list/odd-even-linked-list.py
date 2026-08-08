# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l=[]
        l1=[]
        l2=[]
        while head:
            l.append(head.val)
            head=head.next
        for i in range(len(l)):
            if i%2==0:
                l1.append(l[i])
            else:
                l2.append(l[i])
        l= l1+ l2
        dummy=ListNode(0)
        ptr=dummy
        for i in l:
            ptr.next=ListNode(i)
            ptr=ptr.next
        return dummy.next


        