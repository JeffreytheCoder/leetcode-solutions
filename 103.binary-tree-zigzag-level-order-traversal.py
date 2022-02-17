#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def valueInQueue(queue):
            level = []
            for node in queue:
               level.append(node.val)
            return level 
        
        if not root:
            return []
        
        res = []
        queue = [root]
        
        while queue:
            if len(res) % 2 == 0:
                res.append(valueInQueue(queue))
            else:
                res.append(valueInQueue(queue[::-1]))
            
            for i in range(len(queue)):
                top = queue.pop(0)
                
                if top.left:
                    queue.append(top.left)
                    
                if top.right:
                    queue.append(top.right)    
                
        return res
        
# @lc code=end

