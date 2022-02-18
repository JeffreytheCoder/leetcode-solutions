#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
# postorder traversal
from os import defpath


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def traverse(root, depth):
            if not root.left and not root.right:
                return depth
            
            left_depth, right_depth = float('inf'), float('inf')
        
            if root.left:
                left_depth = traverse(root.left, depth + 1)
                
            if root.right:
                right_depth = traverse(root.right, depth + 1)
        
            return min(left_depth, right_depth)
        
        return traverse(root, 1)
    
# recursive alternative
# bypass depth argument and add 1 to returned depth from postorder traversal
class Solution:
    def minDepth(self, root):
        def getDepth(root):
            if not root:
                return 0
            
            left_depth = getDepth(root.left)
            right_depth = getDepth(root.right)
            
            if root.left and not root.right:
                return 1 + left_depth
            
            if root.right and not root.left:
                return 1 + right_depth
            
            return 1 + min(left_depth, right_depth)
        
        return getDepth(root)
    
# iterative
# levelorder check if leave, return depth
class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        
        queue = [root]
        depth = 0
        
        while queue:
            depth += 1
            
            for i in range(len(queue)):
                top = queue.pop(0)
                
                if not top.left and not top.right:
                    return depth
                
                if top.left:
                    queue.append(top.left)
                    
                if top.right:
                    queue.append(top.right)

# @lc code=end

