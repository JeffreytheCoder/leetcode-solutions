#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start

# string, iterative [1/5]

# key: longest possible prefix is the common substrings between the shortest string and other strings
# e.g. flower, flight, flow. Shortest is flow and common substrings with others is "fl"

# set prefix to the shortest string
# iterate prefix:
#   check each other string if it has same char on the same idx
#   if not return substring of prefix up to this idx
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = min(strs, key=len)

        for i, char in enumerate(prefix):
            for str in strs:
                if str[i] != char:
                    return prefix[:i]

        return prefix

# @lc code=end
