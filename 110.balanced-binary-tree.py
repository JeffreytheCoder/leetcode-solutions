#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
# postorder traversal: 
#   return depth of current node: 
#       1 + max depth of left and right subtree: 
#       return -1 if left and right diff > 1 
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getDepth(root):
            if not root:
                return 0
            
            left_depth = getDepth(root.left)
            right_depth = getDepth(root.right)
            
            if left_depth == -1 or right_depth == -1:
                return -1
            
            if abs(left_depth - right_depth) > 1:
                return -1
            
            return 1 + max(left_depth, right_depth)
        
        return False if getDepth(root) == -1 else True
    
# time: O(n)
# space: O(log n)
        
# @lc code=end

