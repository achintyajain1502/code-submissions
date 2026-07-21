# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        l=[]
        def v(p):
            if not  p:
                return None
            l.append(p.val)
            return v(p.left) or v(p.right)
        v(root)
        return l
        