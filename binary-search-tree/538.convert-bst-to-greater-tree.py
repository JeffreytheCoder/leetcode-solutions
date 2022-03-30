#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# bst[2/5]
# reverse-preorder: right, root, left
# use global pre value to add current node value with pre value

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pre = 0
        def traverse(root):
            nonlocal pre
        
            if not root:
                return
            traverse(root.right)
            root.val += pre
            pre = root.val
            traverse(root.left)
            
        traverse(root)
        return root
        
        
# @lc code=end

