# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
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
        l.sort()
        k=[]
        for i in l:
            if i not in k:
                k.append(i)
        if len(k)==1:
            return -1
        else:
            return k[1]
        