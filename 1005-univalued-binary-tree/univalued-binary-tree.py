# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        l=set()
        def v(p):
            if not p:
                return None
            l.add(p.val)
            return v(p.left) or v(p.right)
        v(root)
        return len(l)==1
        