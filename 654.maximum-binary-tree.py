#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# difficulty: 2/5

# recursive preorder
#   build node with max value
#   build left and right with left and right subarrays
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        cur = max(nums)
        cur_idx = nums.index(cur)
        root = TreeNode(cur)
        
        root.left = self.constructMaximumBinaryTree(nums[:cur_idx])
        root.right = self.constructMaximumBinaryTree(nums[cur_idx + 1:])
        
        return root

# time: O(n)
# space: O(log n)
        
# @lc code=end

