#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start

# hashmap[1/5]

# use hashmap to store last appearance of a char
# track start idx of current nonrepeated substring
# if encounter repeated character:
#   update start idx to next char (next nonrepeated char)
#   update max len (of nonrepeated substring)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_idx = {}
        start = 0
        max_len = 0

        for i, ch in enumerate(s):
            if ch in last_idx and last_idx[ch] >= start:
                start = last_idx[ch] + 1
            else:
                max_len = max(max_len, i - start + 1)

            last_idx[ch] = i

        return max_len

    # O(n)

# @lc code=end
