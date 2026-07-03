# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        l=[]
        for i in lists:
            while i!=None:
                l.append(i.val)
                i=i.next
        l.sort()
        dummy=ListNode(0)
        ptr=dummy
        for i in l:
            ptr.next=ListNode(i)
            ptr=ptr.next
        return dummy.next
        