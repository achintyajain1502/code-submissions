# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        l=set()
        def v(root):
            if not root:
                return 0
            l.add(root.val)
            return v(root.left) or v(root.right)
        v(root)
        m=float('inf')
        l=list(l)
        l.sort()
        for i in range(len(l)-1):
            m=min(m,l[i+1]-l[i])
        return m

