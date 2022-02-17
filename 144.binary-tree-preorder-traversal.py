#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traversal(root):
            if not root:
                return 
            res.append(root.val)
            traversal(root.left)
            traversal(root.right)
        
        traversal(root)
        return res
    
# iterative
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        stack = [root]
        
        while stack:
            top = stack.pop()
            res.append(top.val)
            
            if top.right:
                stack.append(top.right)
                
            if top.left:
                stack.append(top.left)
            
        return res
    
# universal bt traversal
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        stack = [root]
        
        while stack:
            top = stack.pop()
            
            if top:
                if top.right:
                    stack.append(top.right)
                    
                if top.left:
                    stack.append(top.left)
                    
                stack.append(top)
                stack.append(None)
        
            else:
                node = stack.pop()
                res.append(node.val)
                
        return res
    
# @lc code=end

