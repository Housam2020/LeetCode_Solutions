# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        self.ans = None
        def dfs(root):
            if not root:
                return False
            left = dfs(root.left)
            right = dfs(root.right)
            cur = root == p or root == q
            if (cur and left) or (cur and right) or (left and right):
                self.ans = root
                return
            return left or right or cur
        
        dfs(root)
        return self.ans



        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        