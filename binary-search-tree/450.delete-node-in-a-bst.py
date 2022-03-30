#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bst[3/5]

# recursive, preorder
# 3 scenarios of replacing the delete node:
#   1. no children, delete and return none
#   2. no right child, return left child, vice versa
#   3. both child, move left child to the most left child of right child, return right child

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key == root.val:
            if not root.left and not root.right:
                del root
                return None
            
            elif not root.left and root.right:
                new_root = root.right
                del root
                return new_root
            
            elif not root.right and root.left:
                new_root = root.left
                del root
                return new_root
            
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                    
                cur.left = root.left
                new_root = root.right
                del root
                return new_root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        return root
    
# time: O(log n)
# space: O(log n)
        
# @lc code=end

