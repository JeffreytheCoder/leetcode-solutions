#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
# preorder
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        left_val = 0
        
        def traverse(root, depth):
            nonlocal max_depth
            nonlocal left_val
            
            if not root:
                return 
            
            if depth > max_depth:
                max_depth = depth
                left_val = root.val
                
            traverse(root.left, depth + 1)
            traverse(root.right, depth + 1)
        
        traverse(root, 1)
        return left_val
    
# iterative
# preorder
class Solution:
    def findBottomLeftValue(self, root):
        if not root:
            return 0
        
        max_depth = 0
        left_val = 0
        nodes = [(root, 1)]
        
        while nodes:
            top = nodes.pop()
            node = top[0]
            depth = top[1]
            
            if depth > max_depth:
                left_val = node.val
                max_depth = depth
                
            if node.right:
                nodes.append((node.right, depth + 1))
                
            if node.left:
                nodes.append((node.left, depth + 1))
                    
        return left_val
        
# @lc code=end

