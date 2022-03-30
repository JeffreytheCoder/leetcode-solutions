#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# bt[3/5]

# recursive, postorder traversal
# return current node when node is p or q
# if left and right both return node, means current node is common ancestor, return
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q or not root:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        elif not left and right:
            return right
        elif left and not right:
            return left
        else:
            return None
        
# time: O(n)
# space: O(log n)
        
# @lc code=end

