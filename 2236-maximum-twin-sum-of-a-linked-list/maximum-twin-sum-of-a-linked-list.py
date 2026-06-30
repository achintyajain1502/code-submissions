# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        l=[]
        k=[]
        while head!=None:
            l.append(head.val)
            head=head.next
        for i in range(len(l)/2):
            k.append(l[i]+l[-i-1])
        return max(k)
        