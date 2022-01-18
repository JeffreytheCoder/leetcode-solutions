#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
# two pointers approach
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
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

# hashmap approach


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
                if target in hashmap and hashmap[target] > (nums[i] == target) + (nums[j] == target):
                    res.add(tuple(sorted([nums[i], nums[j], target])))

        return res

# @lc code=end
