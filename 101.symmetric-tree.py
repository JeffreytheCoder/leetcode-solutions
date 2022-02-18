#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
# postorder: return bool
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def compare(left, right):
            if not left and right:
                return False
            
            elif not right and left:
                return False
            
            elif not left and not right:
                return True
            
            elif left.val != right.val:
                return False
            
            return compare(left.right, right.left) and compare( left.left, right.right)
        
        if not root:
            return True
        
        return compare(root.left, root.right)
        
# iterative
# not a specific traversal order: use queue to append and pop comparing pair of nodes
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        
        queue = [root.left, root.right]
        
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            
            if not left and right:
                return False
            
            if left and not right:
                return False
            
            if not left and not right:
                continue
            
            if left.val != right.val:
                return False
            
            queue.append(left.left)
            queue.append(right.right)
            
            queue.append(left.right)
            queue.append(right.left)
            
        return True
        
# @lc code=end

