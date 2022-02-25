#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# iterative
# level order recursion
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        count = 0
        queue = [root]
        
        while queue:
            for i in range(len(queue)):
                top = queue.pop(0)
                
                if top.left:
                    queue.append(top.left)
                    
                if top.right:
                    queue.append(top.right)
                
            count += 1
            
        return count

# @lc code=end

