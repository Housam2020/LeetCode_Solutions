# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if p.val > q.val:
            p, q = q, p

        left, right = None, None
        if root == p or root == q or root.val > p.val and root.val < q.val:
            return root
        elif root.val < p.val and root.val < q.val:
            left = self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            right = self.lowestCommonAncestor(root.left, p, q)
        return left or right




        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        