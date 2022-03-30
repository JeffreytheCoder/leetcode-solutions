#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive
# preorder: add val of same node of two trees

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        
        if not root1:
            return root2
        
        if not root2:
            return root1
         
        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root

# time: O(n)
# space: O(1)

# iterative preorder
# use first tree directly to add value of second tree
# use queue to push and pop two nodes of the two trees together, like lc-101 check symmetric tree

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        
        if not root2:
            return root1
        
        queue = [root1, root2]
        
        while queue:
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            node1.val += node2.val
            
            if node1.left and node2.left:
                queue.append(node1.left)
                queue.append(node2.left)
                
            if node1.right and node2.right:
                queue.append(node1.right)
                queue.append(node2.right)
                
            if not node1.left and node2.left:
                node1.left = node2.left
                
            if not node1.right and node2.right:
                node1.right = node2.right
                
        return root1
    
# time: O(n)
# space: O(n)

# @lc code=end

