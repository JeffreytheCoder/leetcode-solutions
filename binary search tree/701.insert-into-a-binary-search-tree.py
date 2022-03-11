#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# bst [1/5]

# recursive, postorder traversal
# same as bst traversal, insert the val at an empty leaf

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
            
        return root
       
# time: O(log n)     
# space: O(log n)

# iterative, postorder traversal
# save parent node when traversing to an empty leaf in loop
# after loop ends, add the new node to the left or right of the parent node

class Solution:
    def insertIntoBST(self, root, val):
        if not root: 
            return TreeNode(val)
        
        parent = None
        cur = root

        while cur: 
            if val > cur.val: 
                parent = cur
                cur = cur.right
                
            elif val < cur.val: 
                parent = cur
                cur = cur.left

        if val < parent.val: 
            parent.left = TreeNode(val)
        else: 
            parent.right = TreeNode(val)
        
        return root
    
# time: O(log n)
# space: O(1)

# @lc code=end

