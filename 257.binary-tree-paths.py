#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
# preorder traversal
#   backtrack push and pop node to path
#   add to paths when reach leaf node
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        path = []
        
        def traverse(root):
            path.append(str(root.val))
            
            if not root.left and not root.right:
                paths.append('->'.join(path))
                return
            
            if root.left:
                traverse(root.left)
                path.pop()
                
            if root.right:
                traverse(root.right)
                path.pop()
        
        traverse(root)   
        return paths
    
# time: O(n)
# space: O(log n) if balanced (every path from root to leaf is height of tree)
#   O(n) worst case if completed unbalanced (store entire tree in path)
            
# iterative
# post order: 
#   use stack to track node to traverse
#   use paths stack to track all previous paths, and the path to current node as the top one in stack
    # can't simply push and pop node to a array like in recursion 
    #   because recursion pops current node after children been traversed
    #   needs further iterates children, so can't pop immediately, otherwise will lose the current node in path
    # append path added with left or right when traverse to left or right
    # pop path when traverse into current nodeand check if leaf node
class Solution:
    def binaryTreePaths(self, root):
        res = []
        paths = [str(root.val)]
        nodes = [root]
        
        while nodes:
            top = nodes.pop()
            path = paths.pop()
            
            if not top.left and not top.right:
                res.append(path)
                
            if top.right:
                nodes.append(top.right)
                paths.append(path + '->' + str(top.right.val))
                
            if top.left:
                nodes.append(top.left)
                paths.append(path + '->' + str(top.left.val))

        return res

# time: O(n)
# space: O(log n) if balanced (every path from root to leaf is height of tree)
#   O(n) worst case if completed unbalanced (store entire tree in path)
    
# @lc code=end

