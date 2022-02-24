#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive
#   locate current node by last element of postorder array
#   split inorder array index of that element
#   split postorder array by length of splitted inorder array
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        cur = postorder[-1]
        root = TreeNode(cur)
        
        cur_idx = inorder.index(cur)
        left_inorder = inorder[:cur_idx]
        right_inorder=inorder[cur_idx + 1:]
        
        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder): len(postorder) - 1]
        
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        
        return root
    
# time: O(n)
# space: O(n)
        
# @lc code=end

