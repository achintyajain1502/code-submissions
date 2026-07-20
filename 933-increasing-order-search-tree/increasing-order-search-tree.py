# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        l=[]
        def v(p):
            if not p:
                return None
            l.append(p.val)
            return v(p.left) or v(p.right)
        v(root)
        l.sort()
        r=TreeNode(l[0])
        ptr=r
        for i in range(1,len(l)):
            ptr.right=TreeNode(l[i])
            ptr=ptr.right
        return r
        