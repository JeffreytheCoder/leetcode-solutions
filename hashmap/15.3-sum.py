#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start

# two pointers [3/5]

# key: num in nums may be repeated, use set to delete repeated three sum tuples

# sort nums
# for each num with idx in nums:
#   set left pointer to idx + 1 and right pointer to last idx
#   check sum of three (num, left, right):
#       if smaller than zero, inc left (nums in ascending order)
#       if larger, dec right
# return nums as set

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for idx, val in enumerate(nums):

            if val > 0:
                break

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                cur = val + nums[left] + nums[right]

                if cur < 0:
                    left += 1
                elif cur > 0:
                    right -= 1
                else:
                    res.add((val, nums[left], nums[right]))
                    left += 1
                    right -= 1

        return res
    
# time: O(n^2)
# space: O(1)

# hashmap [3/5]

# key: num in nums may be repeated, use set to delete repeated three sum tuples
#   make sure three value are distinct elements in nums, use hashmap to store appearance

# like twosum (lc-1), store {num in nums: appearance time of num in nums} in hashmap
# nested for loop i, j in nums:
#   check if target (-(nums[i] + nums[j])) is in hashmap:
#       check target isn't nums[i] or nums[j] (3 value are distinct)
#       if appearance of target value is more than times nums[i] and nums[j] equals to target value, add tuple of three value
# return nums as set
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        res = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])
                # make sure target isn't nums[i] or nums[j]
                if target in hashmap and hashmap[target] > (nums[i] == target) + (nums[j] == target):
                    res.add(tuple(sorted([nums[i], nums[j], target])))

        return res
    
# time: O(n^2)
# space: O(n)

# @lc code=end
