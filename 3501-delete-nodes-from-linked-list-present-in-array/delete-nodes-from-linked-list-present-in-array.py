# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums=set(nums)
        dmy=ListNode(0)
        ptr=dmy
        while head:
            if head.val not in nums:
                ptr.next=ListNode(head.val)
                ptr=ptr.next
            head=head.next
        return dmy.next
        