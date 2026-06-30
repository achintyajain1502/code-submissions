# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        l=[]
        while head!=None:
            l.append(head.val)
            head=head.next
        print l
        i=left-1
        j=right-1
        k=ListNode(0)
        ptr=k
        while i<=j:
            l[i],l[j]=l[j],l[i]
            i+=1
            j-=1
        for i in l:
            ptr.next=ListNode(i)
            ptr=ptr.next
        return k.next
        