# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        l=[]
        def v(p):
            if not p:
                return None
            l.append(p.val)
            return v(p.left) or v(p.right)
        v(root)
        l=l[1:]
        ptr=root
        for i in l:
            ptr.right=TreeNode(i)
            ptr.left=None
            ptr=ptr.right

       