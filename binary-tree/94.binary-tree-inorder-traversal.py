#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(root):
            if not root:
                return
            
            traverse(root.left)
            res.append(root.val)
            traverse(root.right)
        
        traverse(root)
        return res

# iterative
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        
        return res        

# universal traversal
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        
        res = []
        stack = [root]
        
        while stack:
            top = stack.pop()
            
            if top:
                if top.right:
                    stack.append(top.right)
                    
                stack.append(top)
                stack.append(None)
                    
                if top.left:
                    stack.append(top.left)
            
            else:
                node = stack.pop()
                res.append(node.val)
                
        return res  

# @lc code=end

