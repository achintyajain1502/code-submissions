# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        def bst(l):
            if not l:
                return None
            mid=len(l)//2
            root=TreeNode(l[mid])
            root.left=bst(l[:mid])
            root.right=bst(l[mid+1:])
            return root
        return bst(l)
