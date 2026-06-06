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
        num1=""
        num2=""
        l3=ListNode(0)
        while l1 is not None:
            num1+=str(l1.val)
            l1=l1.next
        while l2 is not None:
            num2+=str(l2.val)
            l2=l2.next
        num1=num1[::-1]
        num2=num2[::-1]
        result=list(str(int(num2)+int(num1)))
        result.reverse()

        ptr=l3
        for i in result:
            ptr.next=ListNode(int(i))
            ptr=ptr.next
        return l3.next