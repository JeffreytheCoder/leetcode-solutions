#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
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
# global min difference value, track previous node
# update min with cur - prev if smaller
# like 98. validate BST, but not returning value, just update global

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        prev = None
        
        def traverse(root):
            nonlocal min_diff
            nonlocal prev
            
            if not root:
                return 
            
            left = traverse(root.left)
            if prev:
                min_diff = min(min_diff, abs(root.val - prev.val))
            prev = root
                
            right = traverse(root.right)
            
        traverse(root)
        return min_diff

# time: O(n)
# space: O(log n)

# iterative, inorder traversal

class Solution:
    def getMinimumDifference(self, root):
        stack = []
        prev = None
        cur = root
        min_diff = float('inf')
        
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
                
            else:
                cur = stack.pop()
                if prev:
                    min_diff = min(min_diff, abs(cur.val - prev.val))
                prev = cur
                cur = cur.right
                
        return min_diff
    
# time: O(n)
# space: O(n)
        
# @lc code=end

