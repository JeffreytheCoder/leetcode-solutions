#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# level order
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        queue = [root]
        
        while queue:
            length = len(queue)
            for i in range(length):
                top = queue.pop(0)
                
                if i != length - 1:
                    top.next = queue[0]
                else:
                    top.next = None
                
                if top.left:
                    queue.append(top.left)
                    
                if top.right:
                    queue.append(top.right)
                    
        return root
        
# @lc code=end

