#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = [root]
        level = []
        
        while queue:
            for i in range(len(queue)):
                top = queue.pop(0)
                level.append(top.val)
                
                if top.left:
                    queue.append(top.left)
                    
                if top.right:
                    queue.append(top.right)
                    
            res.append(level)
            level = []
                
        return res
            
        
# @lc code=end

