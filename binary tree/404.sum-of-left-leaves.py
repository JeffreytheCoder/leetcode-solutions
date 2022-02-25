#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def getSum(root):
            if not root:
                return 0
            
            left_val = 0
            if root.left and not root.left.left and not root.left.right:
                left_val = root.left.val 
            
            return left_val + getSum(root.left) + getSum(root.right)
        
        return getSum(root)
    
# time: O(n)
# space: O(log n)

# iterative
# preorder
class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        
        sum_leaves = 0
        nodes = [root]
        
        while nodes:
            top = nodes.pop()
            
            if top.left and not top.left.left and not top.left.right:
                sum_leaves += top.left.val
                
            if top.right:
                nodes.append(top.right)
                
            if top.left:
                nodes.append(top.left)
                
        return sum_leaves
    
# time: O(n)
# space: O(n)

# @lc code=end

