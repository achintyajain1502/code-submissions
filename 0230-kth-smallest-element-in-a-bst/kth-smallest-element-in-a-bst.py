# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        l=[]
        def dfs(root):
            if not root:
                return None
            left=dfs(root.left)
            l.append(root.val)
            right=dfs(root.right)
        dfs(root)
        return l[k-1]
        