#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive
#   locate current node value by first element of preorder array
#   split inorder array by index of that element
#   split preorder array by length of splitted inorder array
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        cur = preorder[0]
        root = TreeNode(cur)
        
        cur_idx = inorder.index(cur)
        left_inorder = inorder[:cur_idx]
        right_inorder = inorder[cur_idx + 1:]
        
        left_preorder = preorder[1: len(left_inorder) + 1]
        right_preorder = preorder[len(left_inorder) + 1 :]
        
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root

# time: O(n)
# space: O(n)
        
# @lc code=end

