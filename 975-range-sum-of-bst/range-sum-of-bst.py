# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        s=0
        if not root:
            return 0
        if low<=root.val<=high:
            s+=root.val
        s+=self.rangeSumBST(root.left,low,high)
        s+=self.rangeSumBST(root.right,low,high)
        return s

        