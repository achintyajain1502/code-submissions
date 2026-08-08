# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        l1=[]
        l2=[]
        def value(root):
            if not root:
                l1.append(None)
                return 
            l1.append(root.val)
            return value(root.left) or value(root.right)
        def value2(root):
            if not root:                
                l2.append(None)
                return
            l2.append(root.val)
            return value2(root.left) or value2(root.right)
        value(p)
        value2(q)
        return l1==l2

        