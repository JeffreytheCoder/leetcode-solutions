#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
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
#   if sum has been found at a leaf, return true
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def traverse(root, count):
            if not root.left and not root.right:
                if count == 0:
                    return True
                else:
                    return False
                
            if root.left:
                if traverse(root.left, count - root.left.val):
                    return True
                
            if root.right:
                if traverse(root.right, count - root.right.val):
                    return True
                
            return False
        
        return traverse(root, targetSum - root.val)
    
# time: O(n)
# space: O(log n)
            
# iterative
# preorder
class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        nodes = [(root, targetSum - root.val)]
        
        while nodes:
            top = nodes.pop()
            node = top[0]
            count = top[1]
            
            if not node.left and not node.right:
                if count == 0:
                    return True
                
            if node.right:
                nodes.append((node.right, count - node.right.val))
                
            if node.left:
                nodes.append((node.left, count - node.left.val))
                
        return False
    
# time: O(n)
# space: O(n)

# @lc code=end

