#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# preorder
# recursive
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if not root:
                return
            
            root.left, root.right = root.right, root.left
            invert(root.left)
            invert(root.right)
            
        invert(root)
        return root

# iterative
class Solution:
    def invertTree(self, root):
        if not root:
            return None
        
        stack = [root]
        
        while stack:
            top = stack.pop()
            top.left, top.right = top.right, top.left
            
            if top.right:
                stack.append(top.right)
                
            if top.left:
                stack.append(top.left)
            
        return root

# @lc code=end

