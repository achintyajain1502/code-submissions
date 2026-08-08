# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        k=l[len(l)/2:]
        k.reverse()
        if len(l)%2==0:
            if l[:len(l)/2]==k:
                return True
        else:
            if l[:len(l)/2]==k[:-1]:
                return True
        return False

        