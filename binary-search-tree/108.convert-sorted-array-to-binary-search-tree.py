#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# bst[2/5]
# recursive, preorder

# build current node as the middle element of the array
# build left and right as recursive result of left and right array

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def traversal(nums: List[int], left: int, right: int) -> TreeNode:
            if left > right:
                return None
            
            mid = left + (right - left) // 2
            mid_root = TreeNode(nums[mid])
            mid_root.left = traversal(nums, left, mid-1)
            mid_root.right = traversal(nums, mid+1, right)

            return mid_root

        return traversal(nums, 0, len(nums) - 1)
        
# @lc code=end

