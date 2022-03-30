#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# bst[2/5]

# recursive, preorder traversal
# like 236.lowest common ancestor of BT, but use characteristic of BST

# current node is common ancestor when value is between [p, q]
# if smaller than both p and q, traverse to right; if larger than both, traverse to left

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        
        if root.val < p.val and root.val < q.val:
            right = self.lowestCommonAncestor(root.right, p, q)
            if right:
                return right
            
        if root.val > p.val and root.val > q.val:
            left = self.lowestCommonAncestor(root.left, p , q)
            if left:
                return left
            
        return root
    
# time: O(n)
# space: O(log n)

# iterative, preorder traversal
# same logic as recursive, but more intuitive

class Solution:
    def lowestCommonAncestor(self, root, p , q):
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root
            
        return None
    
# time: O(n)
# space: O(1)
        
# @lc code=end

