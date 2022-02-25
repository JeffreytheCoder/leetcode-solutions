#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

# hashmap [1/5]
# for each num in nums:
#   store {num : idx} in hashmap
#   if there is a key in hashmap as (target - num), it means two numbers adds up to target,
#       return the idx of num and idx of the key in hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for idx, val in enumerate(nums):
            if (target - val) in dict:
                return [idx, dict[target - val]]
            else:
                dict[val] = idx
                
# time: O(n)
# space: O(n)
        
# @lc code=end

