# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        l=[]
        while head.next:
            l.append(head.next.val)
            head.next=head.next.next
        i=0
        j=len(l)-1
        while i<j:
            head.next=ListNode(l[j])
            head=head.next
            head.next=ListNode(l[i])
            head=head.next
            i+=1
            j-=1
        if len(l)%2!=0:
            head.next=ListNode(l[len(l)/2])


        