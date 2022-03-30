#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bst[1/5]

# recursive
# larger go left, smaller go right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == val:
            return root
        
        if root.val < val:
            return self.searchBST(root.right, val)
        
        if root.val > val:
            return self.searchBST(root.left, val)
        
# time: O(log n)
# space: O(log n)

# iterative
class Solution:
    def searchBST(self, root, val):
        while root:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            else:
                root = root.left
                
        return None
    
# time: O(log n)
# space: O(1)

# @lc code=end

