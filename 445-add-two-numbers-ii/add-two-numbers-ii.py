# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        n1=""
        n2=""
        while l1:
            n1+=str(l1.val)
            l1=l1.next
        while l2:
            n2+=str(l2.val)
            l2=l2.next
        k=list(str(int(n1)+int(n2)))
        dmy=ListNode(0)
        ptr=dmy
        for i in k:
            ptr.next=ListNode(int(i))
            ptr=ptr.next
        return dmy.next
        