#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bst[2/5]

# recursive, inorder traversal
# update max value at each node
#   if current node value < max, means there are nodes larger in the left subtree, return false
# return if left, right and current are valid bst

class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_val = float('-inf')
        
        def isValid(root):
            nonlocal max_val
            if not root:
                return True
            
            left = isValid(root.left)
            
            if root.val > max_val:
                max_val = root.val
            else:
                return False
            
            right = isValid(root.right)
            
            return left and right
        
        return isValid(root)
    
# time: O(n)
# space: O(log n)
    
# iterative, inorder traversal
# more intuitive than recursive, check if the current node is larger than previous node
class Solution:
    def isValidBST(self, root):
        stack = []
        cur = root
        prev = None
        
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if prev and cur.val <= prev.val:
                    return False
                prev = cur
                cur = cur.right
                
        return True

# time: O(n)
# space: O(n)
        
# @lc code=end

