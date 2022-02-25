#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

# hashmap [1/5]

# key: to achieve single loop, find another value that adds up to target with iterated value
#   use hashmap to store {num in nums: its idx}

# for each (num, idx) in nums:
#   if (target - num) is in hashmap, return idx and hashmap[target - num]
#   else store {num: idx} to hashmap

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

