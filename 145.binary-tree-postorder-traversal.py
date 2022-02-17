#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def traverse(root):
            if not root:
                return
            
            traverse(root.left)
            traverse(root.right)
            res.append(root.val)
            
        traverse(root)
        return res
    
class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        
        res = []
        stack = [root]
        
        while stack:
            top = stack.pop()
            res.append(top.val)
            
            if top.left:
                stack.append(top.left)
            
            if top.right:
                stack.append(top.right)
                
        return res[::-1]
    
class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        
        res = []
        stack = [root]
        
        while stack:
            top = stack.pop()
            
            if top:
                stack.append(top)
                stack.append(None)
                
                if top.right:
                    stack.append(top.right)
                    
                if top.left:
                    stack.append(top.left)
                    
            else:
                node = stack.pop()
                res.append(node.val)
                
        return res
        
# @lc code=end

