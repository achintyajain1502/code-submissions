# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l=[]
        s=0
        while head:
            if head.val!=0:
                s+=head.val
                head=head.next
            else:
                l.append(s)
                s=0
                head=head.next
        l=l[1:]
        dmy=ListNode(0)
        ptr=dmy
        for i in l:
            ptr.next=ListNode(i)
            ptr=ptr.next
        return dmy.next
        

        